import * as React from 'react';
import { Socket } from './Socket';

export default function Timeline() {
    
    const [posts, setPosts] = React.useState([]); 
    
    function getPosts() {
        React.useEffect( () => {
            Socket.on('emit posts channel', updatePosts);
            return () => {
                Socket.off('emit posts channel', updatePosts);
            };
        });
    }
    
    function updatePosts(data) {
        setPosts( [data].concat(posts) );
    }
    
    getPosts();
    
    return (
        <div>
        <ul className="timeline">
            { posts.map( (post, index) => (
                <li key={index} className="post">
                    <span className="username"> { post.username } </span> <br />
                    <span className="text"> { post.text } </span> <br />
                    <span className="likes"> &hearts; { post.num_likes } </span> <br />
                </li>
                ))
            }
        </ul>
        </div>
    );
}