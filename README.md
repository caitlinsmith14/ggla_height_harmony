## The Gestural Gradual Learning Algorithm: Height Harmony Edition

On this page, you'll find all of the supplementary materials for our [AMP 2020](https://babel.ucsc.edu/~amp2020/) submission:

Smith, Caitlin, Charlie O'Hara (2020) [Learnability of Derivationally Opaque Patterns in the Gestural Harmony Model](https://padlet.com/AMP2020/posters3). Poster presented at the 2020 Annual Meeting on Phonology, Santa Cruz, CA (Online), September 2020.

### Background Reading

The gestural analysis of stepwise height harmony in Nzebi referenced on our poster is spelled out in greater detail in the paper [Stepwise height harmony as partial transparency](https://pages.jh.edu/~csmit372/pdf/smith_nels50_paper.pdf) (to appear in the proceedings of NELS 50). More papers on the Gestural Harmony Model are available on [Caitlin Smith's website](https://pages.jh.edu/~csmit372/).


### Code Walkthrough

This project introduces the Gestural Gradual Learning Algorithm (GGLA), an error-driven online learning algorithm, and applies it to the task of learning derivationally opaque height harmony patterns. The code we use for computational modeling of the learning of height harmony can be found in `ggla_height_harmony.py` above. Here, we will walk you through how to use this code.

**Check python version and install dependencies.** The code for the GGLA height harmony learner is written for use with python 3.8. It is likely compatible with some older versions of python 3, but we make no guarantees. The code uses several packages that are not included in the python standard library and must be installed by the user. These are: matplotlib (pip install), numpy (conda/pip install), and tqdm (pip install).

**Create a new model language from a harmony pattern file.** A pattern file should be a .json file containing a python dictionary specifying a model language's vowel inventory, how each vowel surfaces in a harmony-conditioning environment, and which vowels trigger harmony. Several sample .json files are included in this repo. Use the Language class to initialize a new model language object.

`>>> model_language = Language(new='stepwise_4.json')`

**Train the model.** Once the model language is initialized, train the height gestures of its vowels and dorsal consonant(s) using the `train_height_strength()` method. This can take anywhere from a few seconds to a minute.

`>>> model_language.train_height_strength()`

Output:

```
156229 [00:03, 42728.35it/s]
Learner converged after 156229 iterations.
```

If the model does not converge after five million iterations, training ceases. If that occurs, you can rerun `train_height_strength()`, which will pick up training right where it left off.

Output:

```
5000000 [01:36, 51501.95it/s]
Learner did not converge after 5000000 iterations.
```

**Inspect the model's results.** For a text display of the final states of the model language's vowel and dorsal consonant inventory, use the `report_training()` method.

`>>> model_language.report_training()`

Output:
```
Trained /i/:
Learner Intrinsic Constriction Degree (CD) 3.9
Learner Blended Constriction Degree (CD) 3.9
Teacher Blended Constriction Degree (CD) 4
Learner Strength 12.7

Trained /u/:
Learner Intrinsic Constriction Degree (CD) 3.9
Learner Blended Constriction Degree (CD) 3.9
Teacher Blended Constriction Degree (CD) 4
Learner Strength 12.7

Trained /e/:
Learner Intrinsic Constriction Degree (CD) 7.9
Learner Blended Constriction Degree (CD) 4.19
Teacher Blended Constriction Degree (CD) 4
Learner Strength 1.0

Trained /o/:
Learner Intrinsic Constriction Degree (CD) 7.9
Learner Blended Constriction Degree (CD) 4.19
Teacher Blended Constriction Degree (CD) 4
Learner Strength 1.0

Trained /ɛ/:
Learner Intrinsic Constriction Degree (CD) 12.1
Learner Blended Constriction Degree (CD) 7.85
Teacher Blended Constriction Degree (CD) 8
Learner Strength 11.8

Trained /ɔ/:
Learner Intrinsic Constriction Degree (CD) 12.1
Learner Blended Constriction Degree (CD) 7.85
Teacher Blended Constriction Degree (CD) 8
Learner Strength 11.8

Trained /a/:
Learner Intrinsic Constriction Degree (CD) 16.1
Learner Blended Constriction Degree (CD) 11.81
Teacher Blended Constriction Degree (CD) 12
Learner Strength 23.4

Trained /g/:
Learner Intrinsic Constriction Degree (CD) -2.0
Learner Blended Constriction Degree (CD) -1.82
Learner Strength 400.2

Learner converged on iteration 156229.
```

To see the trajectories of the learning of each phoneme's constriction degree target and blending strength, use the plot_training() method.

`>>> model_language.plot_training()`

![](https://pages.jh.edu/~csmit372/pic/trajectories.png)

**Save the model.** To save the model for inspection at another time, use the save() method. This creates a human-readable .json file containing a python dictionary with all of the model's parameters and results.

`>>> model_language.save()`

Output:

`Saving model as stepwise_4_model_1.json.`

To export the results of training to tab-delimited text files, use the export_trajectories() method.

`>>> model_language.export_trajectories()`

**Load a pretrained model.** To load a previously trained and saved model, use the Language class to initialize a new model language object and provide it with a .json model file.

`>>> model_language2 = Language(load='stepwise_4_model_1.json')`

Output

`Loading stepwise_4_model_1.json.`

### Investigating Alternatives

We also conducted modeling of height harmony learning in several alternative frameworks. Details can be found in the `alternatives` directory above.
