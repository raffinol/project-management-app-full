import { Link } from "react-router-dom";

function Home({ user, setUser }) {

    if (user) {
      return (
        <>
          <h1>Welcome, {user.username}!</h1><br></br>
        </>
      );
    } else {
      return (
        <>
            <h2>Please Login or Sign Up</h2>
        </>
      );      
    }
  }
  
  export default Home;