import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {useParams, useNavigate} from 'react-router-dom';
import {useCart} from '../contexts/CartContext';
import {BsFillCartFill} from 'react-icons/bs';
import ImageComponent from './ImageComponent';

const BookDetails =()=>{
const {bookId} = useParams();
const [book, setBook] = useState(null);
const {addToCart} = useCart();
const navigate = useNavigate();

    useEffect(() => {
            const fetchBook = async () => {
            try{
                const response=await axios.get(`http://localhost:3001/books/${bookId}`);
                setBook(response.data);
            }catch(error){
                console.error('Error fetching book details:', error);
            }
        };
        fetchBook();
    }, [bookId]);

    const handleAddToCart = (book) => {
        addToCart(book);
        navigate(`/cart`);
    }

    if (!book){
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h2>Book Details</h2>
             <ImageComponent
                 src={book.imageUrl}
                 alt={book.title}
                 style={{ width: '200px', height: 'auto' }}
                fallbackSrc="/book-placeholder.jpg"
              />
            <h3>{book.title}</h3>
            <p>By: {book.author}</p>
            <p>ISBN: {book.isbn}</p>
            <p>Price: ${book.price}</p>
            <button onClick={() => handleAddToCart(book)}> <BsFillCartFill /></button>
        </div>
    );
};

export default BookDetails;