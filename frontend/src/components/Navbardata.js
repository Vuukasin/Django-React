import React, { useState, useEffect, Component } from 'react'
import { render } from 'react-dom'
import { createRoot } from 'react-dom/client'
import axios from 'axios'

const likee = 1

class ProfileStats extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }

    componentDidMount() {

        axios.get('http://127.0.0.1:8000/api/post-stream/')
            .then(data => {
                this.setState(() => {
                    return {
                        data: data.data,
                        loaded: true
                    };
                });
            })
            .catch(err => {
                console.log(err)
            })
    }

    render() {

        return (
            <div>
                {this.state.data.map(post => {
                    return (
                        <div className='asd' key={post.uuid}>
                            <h1>{post.username}</h1>
                            <img src={post.image}></img>
                            <p>{post.like_count}</p>
                            <p>{post.comment_count}</p>
                            <img className='post-avatar' src={post.avatar_url}></img>
                        </div>
                    )
                })}
            </div>
        )
    }
}



const container = document.getElementById('app');
const root = createRoot(container);
root.render(<ProfileStats />)

