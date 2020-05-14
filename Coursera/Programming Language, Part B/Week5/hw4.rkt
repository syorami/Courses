
#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below

;; Problem 1
(define (sequence l h s)
  (if (<= l h) (cons l (sequence (+ l s) h s)) null))

;; Problem 2
(define (string-append-map xs suffix)
  (map (lambda (x) (string-append x suffix)) xs))

;; Problem 3
(define (list-nth-mod xs n)
  (cond [(negative? n) (error "list-nth-mod: negative number")]
        [(null? xs) (error "list-nth-mod: empty list")]
        [#t (let ([remain (remainder n (length xs))])
              (car (list-tail xs remain)))]))

;; Problem 4
(define (stream-for-n-steps s n)
  (if (= n 0)
      null
      (let ([res (s)])
        (cons (car res) (stream-for-n-steps (cdr res) (- n 1))))))

;; Problem 5
(define (funny-number-stream)
  (define (f n) (cons (if (= (remainder n 5) 0) (- n) n) (lambda () (f (+ n 1)))))
  (f 1))

;; Problem 6
(define (dan-then-dog)
  (define (f n) (cons (if (= (remainder n 2) 1) "dan.jpg" "dog.jpg") (lambda () (f (+ n 1)))))
  (f 1))

;; Problem 7
(define (stream-add-zero s)
  (define (f s) (cons (cons 0 (car (s))) (lambda () (f (cdr (s))))))
  (lambda () (f s)))

;; Problem 8
(define (cycle-lists xs ys)
  (define (f n) (cons (cons (list-nth-mod xs n) (list-nth-mod ys n)) (lambda () (f (+ n 1)))))
  (lambda () (f 0)))

;; Problem 9
(define (vector-assoc v vec)
  (define (traverse idx)
    (if (>= idx (vector-length vec))
        #f
        (let ([vi (vector-ref vec idx)])
          (cond [(not (pair? vi)) (traverse (+ idx 1))]
                [(equal? (car vi) v) vi]
                [#t (traverse (+ idx 1))]))))
  (traverse 0))

;; Problem 10
(define (cached-assoc xs n)
  (define cache (make-vector n #f))
  (define idx 0)
  (define (traverse v)
    (let ([cache-ans (vector-assoc v cache)])
      (if cache-ans
          cache-ans
          (let ([xs-ans (assoc v xs)])
            (begin
              (when xs-ans
                (vector-set! cache idx xs-ans)
                (set! idx (remainder (+ idx 1) n))
              xs-ans))))))
  traverse)

; Problem 11
(define-syntax while-less
  (syntax-rules (do)
    [(while-less e1 do e2)
     (letrec ([res1 e1]
              [compare (lambda (res1 res2)
                         (if (>= res2 res1) #t (compare res1 e2)))])
       (compare res1 e2))]))
