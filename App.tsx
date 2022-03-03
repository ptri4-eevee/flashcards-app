import React, { useEffect, useState } from 'react';
import { ActivityIndicator } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Patterns from "./flashcards_react_native/src/screens/Patterns";
import Flashcards from './flashcards_react_native/src/screens/Flashcards';
import storePatterns from './flashcards_react_native/src/store';
import Login from './flashcards_react_native/src/screens/Login';

export type StackParamList = {
    "Common Patterns": Array<{title: string, desc: string}>,
    "Flashcards": any,
    "Login": any,
};

const Stack = createNativeStackNavigator<StackParamList>();
let json: string | any[] = [];

const App = () => {

  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState<any>([]);

  const fetchPatterns = async() => {
    await fetch('/', {
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    })
    .then((res) => res.json())
    .then((fetch) => {
       if(Array.isArray(fetch) && json.length > 0) {
         json = fetch;
       }
    })
    .then(() => {
      (setLoading(false));
  })
  .catch(err => {
    console.log('Error on fetch: ', err)
  })
};

  useEffect(() => {
    const fetch:any = fetchPatterns();
    console.log(fetch.result);
    if(fetch.result === undefined) {
      setData(storePatterns)
    }else{
        setData(json)
    }
  }, []);

  return (
    <NavigationContainer >        
        <Stack.Navigator screenOptions={{
        headerTitleAlign: 'center',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }} initialRouteName="Common Patterns">
          <Stack.Screen name="Common Patterns">
                {(props) => <Patterns {...props} store={data} />}
          </Stack.Screen>
          <Stack.Screen name="Flashcards" component={Flashcards} />
           <Stack.Screen name="Login" component={Login} />
        </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;