// frontend/src/components/BookCard.js
import React from 'react';
import { Link } from 'react-router-dom';
import { Card, Button } from 'react-bootstrap';
import '../styles/BookCard.css';

const BookCard = ({ book }) => {
  return (
    <Card className="book-card card-hover-effect">
      <div className="book-image-container">
        <Card.Img
          variant="top"
          src={book.imageUrl}
          alt={book.title}
          className="book-cover"
          onError={(e) => {
            e.target.onerror = null;
            e.target.src = '/book-placeholder.jpg';
          }}
        />
      </div>
      <Card.Body className="d-flex flex-column">
        <Card.Title className="book-title">{book.title}</Card.Title>
        <Card.Text className="book-author">By: {book.author}</Card.Text>
        <Card.Text className="book-price">Price: ${book.price}</Card.Text>
        <Link to={`/books/${book.id}`} className="mt-auto">
          <Button variant="primary" className="view-book-btn">
            View Book
          </Button>
        </Link>
      </Card.Body>
    </Card>
  );
};

export default BookCard;
