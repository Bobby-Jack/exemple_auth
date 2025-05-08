import React, {useState} from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
export default function Login() {
    const [formdata, setFormdata] = useState({
        username: "",
        password : ""
    })
    const nav = useNavigate()
    const handlechange = (e) => {
    const {id,value} = e.target
    setFormdata({...formdata, [id]: value})
    }

    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError('');
        setSuccess('');
        const response = await axios.post('http://127.0.0.1:8000/api/connexion/',formdata )
        console.log(response);
        const accessToken = await response.data.access_token
        console.log(accessToken);
        localStorage.setItem('access_token', accessToken)
        if (response.data.status === 'success'){
            console.log(accessToken);
            
        }
        else{
            console.log('bru');
            
            
        }

    };


  return (
    <div>
        <h2>Login</h2>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        {success && <p style={{ color: 'green' }}>{success}</p>}
        <form onSubmit={handleSubmit}>
            <label htmlFor="username">username</label>
            <input
                        type="text"
                        id="username"
                        value={formdata.username} onChange={ (e)=>{handlechange(e)}}
                        required
                    />
            <label htmlFor="password">password</label>
            <input
                        type="password"
                        id="password"
                        value={formdata.password} onChange={ (e)=>{handlechange(e)}}
                        required />

            <button type="submit">S'inscrire</button>
        </form>
    </div>
  )
}
