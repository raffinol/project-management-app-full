import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import SignUp from "./SignUp";
import Home from "./Home";
import Login from "./Login";

function App() {
  const [user, setUser] = useState(null);
  const [errors, setErrors] = useState([])

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      } else {
        r.json().then(err => setErrors(err))
      }
    });
  }, []);

  return (
    <>      
      {user ? (
          <Route path="/">
            <Home user={user} setUser={setUser}/>
          </Route>
      ) : (
          <main>
            <Switch>
              <Route path="/signup">
                <SignUp setUser={setUser} />
              </Route>
              <Route path="/login">
                <Login setUser={setUser} />
              </Route>
              <Route path="/">
                <Home />
              </Route>
            </Switch>
          </main>
      )}
    </>
  );
}

export default App;
