import React from 'react';
import { Link } from 'react-router-dom';
import ImageComponent from './ImageComponent';
import '../styles/BookCard.css';
import { Card, Button } from 'react-bootstrap';

const BookCard = ({ book }) => {
    return (
        <Card style={{ height: '100%', display: 'flex', flexDirection: 'column', border:'1px solid lightgray'}}>
            <div style={{
               height: '250px',
                 width: '100%',
                overflow: 'hidden',
                 display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
                }}>
                 <Card.Img variant="top" as={ImageComponent}
                     src={book.imageUrl}
                     alt={book.title}
                     style={{  objectFit: 'contain', maxWidth: '100%', maxHeight: '100%' }}
                     fallbackSrc="/book-placeholder.jpg"
                 />
            </div>
            <Card.Body style={{flexGrow:1, display:'flex', flexDirection:'column', justifyContent:"space-between"}}>
                 <div>
                  <Card.Title>{book.title}</Card.Title>
                  <Card.Text>By: {book.author}</Card.Text>
                   <Card.Text>Price: ${book.price}</Card.Text>
                 </div>
               <Link to={`/books/${book.id}`}>
                    <Button variant="primary">View Book</Button>
                </Link>
           </Card.Body>
        </Card>
    );
};

export default BookCard;