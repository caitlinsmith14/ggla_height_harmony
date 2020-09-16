from copy import deepcopy
import json
import math
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np
import os.path
import random
from tqdm import tqdm


class Segment:  # Segment object class made up of attributes from Gesture object class

    def __init__(self, symbol='', lip=None, tt=None, tb_upper=None, tb_back=None, tr=None, velum=None, glottis=None):
        self.symbol = symbol  # IPA or some other symbol for a segment
        self.lip_gest = lip
        self.tt_gest = tt
        self.tb_upper_gest = tb_upper
        self.tb_back_gest = tb_back
        self.tr_gest = tr
        self.velum_gest = velum
        self.glottis_gest = glottis

    def add_gest(self, gest_type, cl, cd):  # add a gesture to the representation of a segment
        setattr(self, gest_type, Gesture(cl, cd))

    def delete_gest(self, gest_type):  # not needed for anything here--maybe later
        setattr(self, gest_type, None)

    def dict(self):  # make Segment object json serializable

        seg_dict = deepcopy(self.__dict__)

        for item in seg_dict:
            if isinstance(seg_dict[item], Gesture):
                seg_dict[item] = deepcopy(seg_dict[item].__dict__)

        return seg_dict


class Gesture:  # Gesture object class with attributes for learner and teacher

    def __init__(self, cl, cd):
        self.cl = cl  # gesture's constriction location being learned by learner (not currently implemented)
        self.cl_teacher = cl  # gesture's constriction location to be learned from teacher (not currently implemented)
        self.cl_list = []  # gesture's constriction location series (not currently implemented)

        self.cd = 16  # gesture's constriction degree being learned by learner (initialized as /a/)
        self.cd_teacher = cd  # gesture's constriction degree to be learned from teacher
        self.cd_list = []  # gesture's constriction degree series (logged throughout training)

        self.strength = random.randint(1, 20)  # gesture's strength (randomly initialized)
        self.strength_list = []  # gesture's strength series (logged throughout training)

    def update_cl(self, rate):  # not currently implemented
        pass

    def log_cl(self):  # not currently implemented
        pass

    def update_cd(self, rate):  # update gesture's constriction degree during training
        if self.cd + rate >= -2:  # as long as constriction degree isn't going below -2...
            self.cd = round(self.cd + rate, 2)  # ...update the constriction degree according to rate

    def log_cd(self):  # keep track of gesture's constriction degree values throughout training
        self.cd_list.append(round(self.cd, 2))

    def update_strength(self, rate):  # update gesture's strength during training
        if self.strength + rate >= 1:  # as long as strength isn't going below 1...
            self.strength = round(self.strength + rate, 2)  # ...update the strength according to rate

    def log_strength(self):  # keep track of gesture's strength values throughout training
        self.strength_list.append(round(self.strength, 2))


class Language:  # class of objects that define a vowel inventory and a height harmony grammar

    def __init__(self, new='', load=''):

        if load:
            print(f'Loading {load}.')
            with open(load) as jsonfile:
                model_dict = json.load(jsonfile)  # imported model as dictionary from .json file

            self.pattern_name = model_dict['pattern_name']
            self.model_name = model_dict['model_name']
            self.pattern = model_dict['pattern']
            self.trigger = model_dict['trigger']
            self.vowels = self.initialize_vowels(model_dict['vowels'])
            self.consonants = self.initialize_consonants(model_dict['consonants'])
            self.convergence_iteration = model_dict['convergence_iteration']
        elif new:
            self.pattern_name = new  # filename for language pattern dictionary from .json file
            self.model_name = ''  # filename for language model .json file

            with open(new) as jsonfile:
                self.pattern = json.load(jsonfile)  # imported harmony pattern as dictionary from .json file

            self.trigger = self.pattern['trigger']  # trigger of height harmony
            self.vowels = self.initialize_vowels()  # create dictionary of all vowels in inventory
            self.consonants = self.initialize_consonants()  # create dictionary of all consonants in inventory
            self.convergence_iteration = -1  # at what iteration does model converge (-1 means no convergence yet)
        else:
            print('Enter either a model filename to load a trained model or a pattern filename to train a new model.')

    def initialize_vowels(self, load=None):  # make all vowels under consideration and put them in a list

        if load:  # if provided with .json dict for loading in saved vowels
            vowels = load  # use the .json dict to create dict of vowels
            for v in vowels:
                for attrib in vowels[v]:
                    if isinstance(vowels[v][attrib], dict):
                        vowels[v][attrib] = json2gest(vowels[v][attrib])  # create Gesture object from dict
                vowels[v] = json2seg(vowels[v])  # create Segment object from dict
        else:  # if creating a new vowel inventory
            vowels = {}  # initialize empty vowel dictionary

            if 'ɛ' in self.pattern:  # if low-mid vowels are in pattern...
                n_heights = 4  # ...then vowel inventory has at least 4 heights
            elif 'e' in self.pattern:  # if mid vowels are in pattern...
                n_heights = 3  # ...then vowel inventory has at least 3 heights
            else:  # if there are no mid vowels in pattern...
                n_heights = 2  # ...then vowel inventory has only 2 heights

            vowels['i'] = Segment('i', tb_upper=Gesture(0, 4), tb_back=Gesture(0, 16))  # add /i/
            vowels['u'] = Segment('u', tb_upper=Gesture(0, 4), tb_back=Gesture(0, 8))  # add /u/

            if n_heights == 3:  # three-height systems get mid vowels
                vowels['e'] = Segment('e', tb_upper=Gesture(0, 10), tb_back=Gesture(0, 16))  # add true mid /e/
                vowels['o'] = Segment('o', tb_upper=Gesture(0, 10), tb_back=Gesture(0, 8))  # add true mid /o/

            elif n_heights == 4:  # four-height systems get high-mid and low-mid vowels
                vowels['e'] = Segment('e', tb_upper=Gesture(0, 8), tb_back=Gesture(0, 16))  # add high-mid /e/
                vowels['o'] = Segment('o', tb_upper=Gesture(0, 8), tb_back=Gesture(0, 8))  # add high-mid /o/
                vowels['ɛ'] = Segment('ɛ', tb_upper=Gesture(0, 12), tb_back=Gesture(0, 16))  # add low-mid /ɛ/
                vowels['ɔ'] = Segment('ɔ', tb_upper=Gesture(0, 12), tb_back=Gesture(0, 8))  # add /low-mid /ɔ/

            vowels['a'] = Segment('a', tb_upper=Gesture(0, 16), tb_back=Gesture(0, 16))  # add /a/

        return vowels

    def initialize_consonants(self, load=None):

        if load:  # if provided with .json dict for loading in saved consonants
            consonants = load  # use the .json dict to create dict of consonants
            for c in consonants:
                for attrib in consonants[c]:
                    if isinstance(consonants[c][attrib], dict):
                        consonants[c][attrib] = json2gest(consonants[c][attrib])  # create Gesture object from dict
                consonants[c] = json2seg(consonants[c])  # create Segment object from dict
        else:  # if creating a new consonant inventory
            consonants = {'g': Segment('g', tb_upper=Gesture(0, -2), tb_back=Gesture(0, -2)),
                          'b': Segment('b', lip=Gesture(0, -2))}

        return consonants

    def train_height_strength(self, rate=0.1, v_window=0.2, c_window=1):

        it = 1  # initialize training trial counter
        progress = tqdm()  # initialize progress bar
        progress.update(1)  # increment progress bar once (so it starts at 1 and not 0)

        while self.convergence_iteration == -1:  # while the model is still learning (not converged)

            # Initialize Gestural Parameter Updates

            v1_strength_update = 0
            v2_strength_update = 0
            c_strength_update = 0

            v1_cd_update = 0
            v2_cd_update = 0
            c_cd_update = 0

            # Make a Random Training Trial #

            n_syll = random.choice(range(1, 3))  # pick one or two syllables randomly each trial
            if n_syll == 1:  # if the trial only has one syllable...
                v1 = None  # ...then there is no v1 (monosyllables are v2 only)
            else:  # otherwise if the trial has two syllables...
                v1 = random.choice(list(self.vowels.values()))  # ...pick any vowel randomly for this trial for v1

            v2 = random.choice(list(self.vowels.values()))  # pick any vowel randomly each trial for v2
            consonant = random.choice(list(self.consonants.values()))  # pick any consonant randomly each trial

            # Consonant Blending with V2 (regardless of syllable count) #

            if consonant.tb_upper_gest is not None:  # if consonant has a TB upper gesture...
                target_c = consonant.tb_upper_gest.cd_teacher  # ...we want the consonant to surface faithfully...
                output_c = blend(consonant.tb_upper_gest, v2.tb_upper_gest, 'cd')  # ...and to blend with v2

                if output_c >= target_c + c_window:  # if the blended c is too open...
                    v2_strength_update += -1 * rate  # ...make the vowel weaker...
                    v2_cd_update += -1 * rate  # ...and higher (smaller CD)...
                    c_strength_update += rate  # ...and make the consonant stronger...
                    c_cd_update += -1 * rate  # ...and higher (smaller CD)

                elif output_c <= target_c - c_window:  # if the blended c is too closed...
                    v2_strength_update += rate  # ...then make the vowel stronger...
                    v2_cd_update += rate  # ...and lower (bigger CD)...

                    c_strength_update += -1 * rate  # ...and make the consonant weaker...
                    c_cd_update += rate  # ...and lower (bigger CD)

            # V2 Target Learning (regardless of syllable count) #

            target_v2 = v2.tb_upper_gest.cd_teacher  # teacher v2 constriction degree
            output_v2 = v2.tb_upper_gest.cd  # learner v2 constriction degree

            if output_v2 >= target_v2 + v_window:  # if learner v2 is too low...
                v2_cd_update += -1 * rate  # ...then make the vowel higher (smaller CD)
            elif output_v2 <= target_v2 - v_window:  # otherwise if learner v2 is too high...
                v2_cd_update += rate  # ...then make the vowel lower (bigger CD)

            # Two Syllable Words #

            if v1 is not None:  # if it's a two-syllable word...

                # Vowel Blending for Harmony

                if v2.symbol in self.trigger:  # ...and if it has a harmony trigger...
                    target_v1 = self.vowels[self.pattern[v1.symbol]].tb_upper_gest.cd_teacher  # ...v1 follows pattern
                    output_v1 = blend(v1.tb_upper_gest, v2.tb_upper_gest, 'cd')  # learner v1 is blend of v1 and v2

                    if output_v1 >= target_v1 + v_window:  # if learner blended vowel is too low...
                        v1_strength_update += -1 * rate  # ...then make the non-high vowel weaker...
                        v1_cd_update += -1 * rate  # ...and higher (smaller CD)
                        v2_strength_update += rate  # and make the high vowel stronger...
                        v2_cd_update += -1 * rate  # ...and higher (smaller CD)

                    elif output_v1 <= target_v1 - v_window:  # if  learner blended v1 is too high...
                        v1_strength_update += rate  # ...then make the non-high v1 stronger...
                        v1_cd_update += rate  # ...and lower (bigger CD)
                        v2_strength_update += -1 * rate  # and make the high v2 weaker...
                        v2_cd_update += rate  # ...and lower (bigger CD)

                # V1 Target Learning (Without Harmony)

                else:  # otherwise for any other (non-harmonizing) vowel sequence...
                    target_v1 = v1.tb_upper_gest.cd_teacher  # teacher v1 surfaces faithfully (same cd)
                    output_v1 = v1.tb_upper_gest.cd  # learner v1 height is v1 (not blended)

                    if output_v1 >= target_v1 + v_window:  # if learner v1 is too low...
                        v1_cd_update += -1 * rate  # ...then make it higher (smaller CD)
                    elif output_v1 <= target_v1 - v_window:  # if learner v1 vowel is too high...
                        v1_cd_update += rate  # ...then make v1 lower (bigger CD)

            # End of Training Trial - Do Gestural Parameter Updates

            if v1 is not None:  # if v1 exists
                v1.tb_upper_gest.update_strength(v1_strength_update)  # update v1 strength
                v1.tb_upper_gest.update_cd(v1_cd_update)  # update v1 constriction degree

            v2.tb_upper_gest.update_strength(v2_strength_update)  # update v2 strength
            v2.tb_upper_gest.update_cd(v2_cd_update)  # update v2 constriction degree

            if consonant.tb_upper_gest is not None:  # if consonant is dorsal
                consonant.tb_upper_gest.update_strength(c_strength_update)  # update consonant strength
                consonant.tb_upper_gest.update_cd(c_cd_update)  # update consonant constriction degree

            # End of Training Trial - Log Trial

            for v in self.vowels.values():  # for each vowel being trained...
                v.tb_upper_gest.log_strength()  # ...log its strength after this trial
                v.tb_upper_gest.log_cd()  # ...and log its constriction degree after this trial
                n_iter = len(v.tb_upper_gest.strength_list)

            for c in self.consonants.values():  # for each consonant being trained...
                if c.tb_upper_gest is not None:  # ...if it has a TB upper gesture...
                    c.tb_upper_gest.log_strength()  # ...then log its strength after this trial
                    c.tb_upper_gest.log_cd()  # ...and log its constriction degree after this trial

            # End of Training Trial - Check for Convergence

            if self.check_convergence(v_window, c_window):  # check if all segments are within their windows
                self.convergence_iteration = n_iter  # record iteration of convergence
                progress.close()
                print(f'Learner converged after {n_iter} iterations.')
            else:
                it += 1  # increment iteration counter
                progress.update(1)  # increment progress bar
                if it > 5_000_000:  # if 5 million iteration cutoff is reached
                    print(f'Learner did not converge after {n_iter} iterations.')
                    break  # stop training

    def check_convergence(self, v_window=0.2, c_window=1):  # check to see if model has converged (no more errors)

        converged = True

        for c in self.consonants:
            consonant = self.consonants[c]
            if consonant.tb_upper_gest is not None:  # check dorsal consonants
                target_c = consonant.tb_upper_gest.cd_teacher  # c should surface faithful to teacher
                for v in self.vowels:  # ...in combination with all vowels (all CV sequences)
                    vowel = self.vowels[v]
                    output_c = blend(consonant.tb_upper_gest, vowel.tb_upper_gest, 'cd')  # CV blending
                    if abs(output_c - target_c) >= c_window:  # if there's a consonant error...
                        converged = False  # ...then the model hasn't converged
                        return converged

        for v in self.vowels:
            vowel = self.vowels[v]
            target_v = vowel.tb_upper_gest.cd_teacher  # v should surface faithful to teacher when no harmony occurs
            output_v = vowel.tb_upper_gest.cd
            if abs(output_v - target_v) >= v_window:  # if there's a vowel error...
                converged = False  # then the model hasn't converged
                return converged

            if vowel.symbol in self.trigger:  # if v is a harmony trigger
                for vowel1 in self.vowels:
                    v1 = self.vowels[vowel1]
                    target_v1 = self.vowels[self.pattern[v1.symbol]].tb_upper_gest.cd_teacher  # v1 should follow pattern
                    output_v1 = blend(v1.tb_upper_gest, vowel.tb_upper_gest, 'cd')  # harmony blending
                    if abs(output_v1-target_v1) >= v_window:  # if there's a harmony error...
                        converged = False  # ...then the model hasn't converged
                        return converged

        return converged

    def plot_training(self):

        colors = pl.cm.viridis(np.linspace(0, 1, len(self.vowels)))  # make a colormap for plotting
        x = 0  # initialize counter for colormap

        plt.figure('Gestural Strength Learning Trajectories')
        plt.subplot(2, 1, 1)

        ymax = 0  # initialize maximum y value for plot

        for v in self.vowels.values():
            if max(v.tb_upper_gest.strength_list) > ymax:
                ymax = max(v.tb_upper_gest.strength_list)  # record new maximum y value
            plt.plot(v.tb_upper_gest.strength_list, '-', color=colors[x], label=v.symbol)  # plot vowel strength
            x += 1  # iterate counter for colormap
            length = len(v.tb_upper_gest.strength_list)
        plt.axis([0, length, 0, plt_round(ymax)])
        plt.legend(bbox_to_anchor=(0, 0, 1, 1), bbox_transform=plt.gcf().transFigure, loc='upper right')

        plt.subplot(2, 1, 2)

        ymax = 0  # initialize maximum y value for plot

        for c in self.consonants.values():
            if c.tb_upper_gest is not None:
                if max(c.tb_upper_gest.strength_list) > ymax:
                    ymax = max(c.tb_upper_gest.strength_list)  # record new maximum y value
                plt.plot(c.tb_upper_gest.strength_list, 'k-', label=c.symbol)  # plot  consonant strength
        plt.axis([0, length, 0, plt_round(ymax)])
        plt.legend(bbox_to_anchor=(0, 0, 1, 1), bbox_transform=plt.gcf().transFigure, loc='center right')

        plt.figure('Constriction Degree Learning Trajectories')

        x = 0  # re-initialize counter for colormap

        for v in self.vowels.values():
            plt.plot(v.tb_upper_gest.cd_list, '-', color=colors[x], label=v.symbol)  # plot vowel constriction degree
            x += 1
        plt.axis([0, length, -5, 20])
        plt.legend(bbox_to_anchor=(0, 0, 1, 1), bbox_transform=plt.gcf().transFigure, loc='upper right')

        for c in self.consonants.values():
            if c.tb_upper_gest is not None:
                plt.plot(c.tb_upper_gest.cd_list, 'k-', label=c.symbol)  # plot consonant constriction degree
        plt.legend(bbox_to_anchor=(0, 0, 1, 1), bbox_transform=plt.gcf().transFigure, loc='center right')

        plt.show()

    def report_training(self):

        for v in self.vowels.values():
            print(f'Trained /{v.symbol}/:\nLearner Intrinsic Constriction Degree (CD) {round(v.tb_upper_gest.cd, 2)}\
                  \nLearner Blended Constriction Degree (CD) \
                  {round(blend(self.vowels[self.trigger[0]].tb_upper_gest, v.tb_upper_gest, "cd"), 2)}\
                  \nTeacher Blended Constriction Degree (CD) \
                  {round(self.vowels[self.pattern[v.symbol]].tb_upper_gest.cd_teacher, 2)}\
                  \nLearner Strength {round(v.tb_upper_gest.strength, 2)}\n')

        for c in self.consonants.values():
            if c.tb_upper_gest is not None:
                print(f'Trained /{c.symbol}/:\nLearner Intrinsic Constriction Degree (CD) {round(c.tb_upper_gest.cd, 2)}\
                      \nLearner Blended Constriction Degree (CD) \
                      {round(blend(self.vowels[self.trigger[0]].tb_upper_gest, c.tb_upper_gest, "cd"), 2)}\
                      \nLearner Strength {round(c.tb_upper_gest.strength, 2)}\n')

        if self.convergence_iteration == -1:
            print(f'Learner did not converge after {len(v.tb_upper_gest.strength_list)} iterations.')
        else:
            print(f'Learner converged after {self.convergence_iteration} iterations.')

    def dict(self):  # make Language object json serializable

        lang_dict = deepcopy(self.__dict__)  # copy object dictionary

        for item in lang_dict['vowels']:
            if isinstance(lang_dict['vowels'][item], Segment):
                lang_dict['vowels'][item] = lang_dict['vowels'][item].dict()  # serialize vowel Segments

        for item in lang_dict['consonants']:
            if isinstance(lang_dict['consonants'][item], Segment):
                lang_dict['consonants'][item] = lang_dict['consonants'][item].dict()  # serialize consonant Segments

        return lang_dict

    def save(self, check_sure=True):

        if self.model_name and check_sure and input(f'Model file {self.model_name} already exists. \
        Do you want to replace it? (y / n)') in ['y', 'Y', 'yes', 'Yes', 'YES']:  # check if sure about replacing
            filename = self.model_name
        else:
            it = 1  # initialize model marker
            while os.path.isfile(f'{self.pattern_name[:-5]}_model_{it}.json'):  # check to see if saved file exists
                it += 1  # if so, iterate its marker until you find one not already in use
            filename = f'{self.pattern_name[:-5]}_model_{it}.json'  # append marker to filename
            print(f'Saving model as {filename}.')

            self.model_name = filename  # record the model's filename

        with open(filename, 'w') as model_json_file:
            json.dump(self.dict(), model_json_file)  # save to current directory
            model_json_file.close()

    def export_trajectories(self):

        if not self.model_name:
            self.save()  # save model if not yet saved

        filename = self.model_name[:-5]

        with open(filename + '_strengths.txt', 'w') as strength_output:  # write strengths to file
            strength_output.write('tb_upper Gestural Strength Learning Trajectories\n')
            for v in self.vowels.values():
                line = v.symbol + '\t' + '\t'.join(str(x) for x in v.tb_upper_gest.strength_list) + '\n'
                strength_output.write(line)
            for c in self.consonants.values():
                if c.tb_upper_gest is not None:
                    line = c.symbol + '\t' + '\t'.join(str(x) for x in c.tb_upper_gest.strength_list) + '\n'
                    strength_output.write(line)
            strength_output.close()

        with open(filename + '_targets.txt', 'w') as target_output:  # write target constriction degrees to file
            target_output.write('tb_upper Gestural Target Learning Trajectories\n')
            for v in self.vowels.values():
                line = v.symbol + '\t' + '\t'.join(str(x) for x in v.tb_upper_gest.cd_list) + '\n'
                target_output.write(line)
            for c in self.consonants.values():
                if c.tb_upper_gest is not None:
                    line = c.symbol + '\t' + '\t'.join(str(x) for x in c.tb_upper_gest.cd_list) + '\n'
                    target_output.write(line)
            target_output.close()

####################
# HELPER FUNCTIONS #
####################


def plt_round(x):
    if x % 50 == 0:
        return x + 10
    else:
        mult = 50 ** -1
        return math.ceil(x*mult) / mult


def blend(gest1, gest2, tract_var):  # blend gestures via average weighted by their strengths
    if tract_var == 'cd':  # if considering constriction degree, blend gestures' degrees
        return ((gest1.cd * gest1.strength) + (gest2.cd * gest2.strength)) / (gest1.strength + gest2.strength)
    elif tract_var == 'cl':  # if considering constriction location, blend gestures' locations
        return ((gest1.cl * gest1.strength) + (gest2.cl * gest2.strength)) / (gest1.strength + gest2.strength)


def json2gest(json_dict):  # parse a .json dictionary into a Gesture object

    gesture = Gesture(None, None)
    gesture.cl = json_dict['cl']
    gesture.cl_teacher = json_dict['cl_teacher']
    gesture.cl_list = json_dict['cl_list']
    gesture.cd = json_dict['cd']
    gesture.cd_teacher = json_dict['cd_teacher']
    gesture.cd_list = json_dict['cd_list']
    gesture.strength = json_dict['strength']
    gesture.strength_list = json_dict['strength_list']

    return gesture


def json2seg(json_dict):  # parse a .json dictionary into a Segment object

    segment = Segment(json_dict['symbol'],
                      json_dict['lip_gest'],
                      json_dict['tt_gest'],
                      json_dict['tb_upper_gest'],
                      json_dict['tb_back_gest'],
                      json_dict['tr_gest'],
                      json_dict['velum_gest'],
                      json_dict['glottis_gest'])

    return segment
