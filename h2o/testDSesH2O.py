#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import autosklearn.classification
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics

from autosklearn.experimental.askl2 import AutoSklearn2Classifier
from autosklearn.classification import AutoSklearnClassifier

import pandas as pd
import numpy as np

if __name__ == "__main__":
    DSes = [
	'airlines.csv', 
	'Amazon_employee_access.csv', 
	'blood-transfusion-service-center.csv', 
	'cifar-10-binary.csv', 
	'connect-4-balanced-binary.csv', 
	'connect-4-imbalanced-binary.csv', 
	'Fashion-MNIST-binary.csv', 
	'jungle_chess_2pcs_raw_endgame_complete-binary.csv', 
	'kc1.csv', 
	'KDDCup09_appetency.csv', 
	'vehicle-binary.csv' 
    ]
    for DS in DSes:
    			
        path = '//home//maksim//Desktop//datasets//binary//'+DS
        print('\n\n'+path+'\n\n')
        
        data = pd.read_csv(path)
        print(data) 
        
        
        # -----! Cast types !-------
        if(DS=='airlines.csv'):
            for column in data.columns:
                print(type(column),column)
                if(column in ['Flight','DayOfWeek','Time','Length'] ):
                    data[column] = pd.to_numeric(data[column])
                elif(column in ['Airline','AirportFrom','AirportTo','Delay'] ):
                    data[column] = data[column].astype('category')
                    #data[column] = data[column].astype('bool') 
                    
        elif(DS=='Amazon_employee_access.csv'):
            for column in data.columns:
                print(type(column),column)
                if(column in ['RESOURCE','MGR_ID','ROLE_ROLLUP_1','ROLE_ROLLUP_2',
                			'ROLE_DEPTNAME','ROLE_TITLE','ROLE_FAMILY_DESC', 
                			'ROLE_FAMILY', 'ROLE_CODE','target'] ):
                    data[column] = data[column].astype('category')
     
        elif(DS=='blood-transfusion-service-center.csv'):
            for column in data.columns:
                print(type(column),column)
                if(column in ['V1','V2','V3','V4'] ):
                    data[column] = pd.to_numeric(data[column])
                elif(column in ['Class'] ):
                    data[column] = data[column].astype('category')

        elif(DS=='cifar-10-binary.csv'):
            for column in data.columns:
                print(type(column),column)
                if(column in ['class'] ):
                    data[column] = data[column].astype('category')
                else:
                    data[column] = pd.to_numeric(data[column])

        elif(DS=='connect-4-balanced-binary.csv' or DS=='connect-4-imbalanced-binary.csv'):
            for column in data.columns:
                print(type(column),column)
                data[column] = data[column].astype('category')
                
        elif(DS=='Fashion-MNIST-binary.csv'):
            for column in data.columns:
                print(type(column),column)
                if(column in ['class'] ):
                    data[column] = data[column].astype('category')
                else:
                    data[column] = pd.to_numeric(data[column])

        elif(DS=='jungle_chess_2pcs_raw_endgame_complete-binary.csv'):
            for column in data.columns:
                print(type(column),column)
                if(column in ['class'] ):
                    data[column] = data[column].astype('category')
                else:
                    data[column] = pd.to_numeric(data[column])
                    
        elif(DS=='kc1.csv'):
            for column in data.columns:
                print(type(column),column)
                if(column in ['defects'] ):
                    data[column] = data[column].astype('category')
                else:
                    data[column] = pd.to_numeric(data[column])
                    
        elif(DS=='KDDCup09_appetency.csv'):
            data = data.replace('?',np.NaN)
            for column in data.columns:
                print(type(column),column)
                if(column in ['Var191','Var192','Var193','Var194','Var195',
                'Var196','Var197','Var198','Var199','Var200','Var201','Var202',
                'Var203','Var204','Var205','Var206','Var207','Var208',
                'Var210','Var211','Var212','Var213','Var214','Var215','Var216',
                'Var217','Var218','Var219','Var220','Var221','Var222','Var223',
                'Var224','Var225','Var226','Var227','Var228','Var229','APPETENCY'] ):
                    data[column] = data[column].astype('category')
                else:
                    data[column] = pd.to_numeric(data[column])

        elif(DS=='vehicle-binary.csv'):
            for column in data.columns:
                print(type(column),column)
                if(column in ['Class'] ):
                    data[column] = data[column].astype('category')
                else:
                    data[column] = pd.to_numeric(data[column])
                    
        # -----!!------
        
        
        X,y = data.iloc[:,:-1] , data.iloc[:,-1:]
        print(X,y)

        X_train, X_test, y_train, y_test = \
              sklearn.model_selection.train_test_split(X, y, random_state=1)

        automl = AutoSklearnClassifier(
        		time_left_for_this_task=30, 
        		resampling_strategy='cv',
        		resampling_strategy_arguments={'folds':5}
        		)
        #automl = AutoSklearn2Classifier(time_left_for_this_task=30)

        automl.fit(X_train, y_train)

        y_hat = automl.predict(X_test)

        print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))
        print(pd.DataFrame(automl.cv_results_))
        
        
        
        
