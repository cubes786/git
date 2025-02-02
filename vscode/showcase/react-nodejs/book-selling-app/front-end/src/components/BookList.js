// frontend/src/components/BookList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import BookCard from './BookCard';
import { Container, Row, Col } from 'react-bootstrap';
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
    <Container className="book-list-container">
      <h2 className="section-title">Book List</h2>
      <Row xs={1} md={3} className="g-4">
        {books.map((book) => (
          <Col key={book.id}>
            <BookCard book={book} />
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default BookList;
