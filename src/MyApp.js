import Table from './Table'
import Form from './Form';
import axios from 'axios';
import React, {useState, useEffect} from 'react';

function MyApp() {

  const [characters, setCharacters] = useState([]);  

  function removeOneCharacter(index){
   makeDeleteCall(characters[index]).then(result => {
   if (result)
   {
      const updated = characters.filter((character,i) => {
         return i !== index
     });
   setCharacters(updated);
   }
   });
}

  function updateList(person) { 
    makePostCall(person).then( result => {
    if (result)
       setCharacters([...characters, result] );
    });
 }

  async function fetchAll(){
    try {
       const response = await axios.get('http://localhost:5000/users');
       return response.data.users_list;     
    }
    catch (error){
       console.log(error); 
       return false;         
    }
 }

 async function makePostCall(person){
  try {
     const response = await axios.post('http://localhost:5000/users', person);
     if(response.status === 201) return response.data;
    else return false;
  }
  catch (error) {
     console.log(error);
     return false;
  }
}
async function makeDeleteCall(person){
  try {
    const response = await axios.delete('http://localhost:5000/users/' + person.id );
    console.log(response)
    if(response.status === 204) return response;
    else return false;     
 }
 catch (error){
    console.log(error); 
    return false;      
 }
}
useEffect(() => {
   fetchAll().then( result => {
      if (result)
         setCharacters(result);
    });
}, [] );

 return (
   <div className="container">
     <Table characterData={characters} removeCharacter={removeOneCharacter} />
     <Form handleSubmit={updateList} />
   </div>
 );
}

export default MyApp;