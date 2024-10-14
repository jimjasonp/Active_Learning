# Active_Learning
                        model training
                     /        |        \
                    /         |         \
                   /          |          \
      model choice    feature training     y_set_creator
        (helper)              |            ~~~DAMAGE DATA~~~~
                              |
                            features
                        /      |      \    
                       /       |       \
                      /        |        \
    sensor_data_list        fourier       feature_maker
    (x_set_creator)         (helper)       (helper)
    ~~~SENSOR DATA~~~~


------Model training------

o xristis eisagei tous sensors to feature to eidos damage to model kai to data percentage
ta dedomena ginointai scale kai trexei to montelo kai bgazei metrics analoga thn periptwsh


------training params------
To function feature for training pairnei to sensor_list kai to feature apo th main pou thelo na ftiaksei 
kai to bazei sthn katallhlh morfh gia training

To function model_choice einai mia domh if / else pou epilegei to modelo pou tha ginei train.
O xristis dinei to x_train x_test kai y_train kai to function bgazei to y_pred


------y_set_creator------
H y_set_creator pairnei ta data gia damage kai kataskeuazei ena df pou bazei tis times twn damage indexes.
Kat ousian h douleia pou kanei einai na taksinomei ta data se auksouysa seira basei tou arithmou tou csv kai epistrefei 
ena df me damage indexes


------main------


kathe sample einai ena timeserie

To programma pairnei ola ta dedomena twn sensors kai efarmozei fft se kathe sample. To feature maker pairnei ta apotelesmata tou fft kai dhmiourgei to antisoixo feature kai to kataxwrei se mia lista

------x_set_creator------

To programma pairnei ta csv me tis metrhseis twn sensors kai ta taksinomei se auksousa seira. Kat ousian
ftiaxnei mia lista me ta timeseries kathe peiramatos.