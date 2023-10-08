import { Link } from "react-router-dom";

function Home({ user }) {
    if (user) {
      return <h1>Welcome, {user.username}!</h1>;
    } else {
      return (
        <>
            <h2>Please Login or Sign Up</h2>
            <Link to="/signup">Signup</Link><br></br>            
            <Link to="/login">Login</Link>

        </>
      );
      
    }
  }
  
  export default Home;