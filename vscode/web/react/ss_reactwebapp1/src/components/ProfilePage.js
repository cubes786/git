import React from 'react';

function ProfilePage({ user }) {
  return (
    <div>
      <h1>Profile</h1>
      <p>Username: {user.username}</p>
      {/*<!-- Add more user
       details here -->*/}
    </div>
  );
}

export default ProfilePage;