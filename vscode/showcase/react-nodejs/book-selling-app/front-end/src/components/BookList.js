import React, { useState, useEffect } from 'react';
import axios from 'axios';
import BookCard from './BookCard';
import { Link } from 'react-router-dom';
import { Row, Col, Container } from 'react-bootstrap';
import '../styles/BookList.css';

const BookList = () => {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        const fetchBooks = async () => {
            try {
                const response = await axios.get('http://localhost:3001/books');
                setBooks(response.data);
            } catch (error) {
                console.error('Error fetching books:', error);
            }
        };
        fetchBooks();
    }, []);

    return (
        <Container>
          <h2 className="mb-4">Book List</h2>
             <div className='top-links'>
                <Link to="/register">Register</Link>
                <Link to="/login">Login</Link>
                <Link to="/profile">Profile</Link>
            </div>
              <Row xs={1} md={3} className="g-4">
                {books.map(book => (
                    <Col key={book.id}>
                       <BookCard book={book} />
                   </Col>
               ))}
           </Row>
        </Container>
    );
};

export default BookList;