;LISP Assignment - CSCI 372
;Spencer Fjelstad
;Problem 1
(format t"(lambda)'(1 2 3 4) returns ~S~%" (mapcar (lambda (lis)(* lis 2)) '(1 2 3 4)))

;Problem 2
(defun MAKE-SET (lis)
    (remove-duplicates lis)
)

;Problem 3
(defun IS-SET (lis)
    (if (equal lis (MAKE-SET lis))
        '(T)
        '(nil)
    )
)

;Problem 4
(defun MY-LEN (lis)
    (if (equal lis nil)
        0
        (+ (MY-LEN (cdr lis)) 1)
    )
)

;Problem 5
(defun MY-SUM (lis)
    (if (equal lis nil)
        0
        (+ (MY-SUM (cdr lis)) (car lis))
    )
)

;Problem 6
(defun MY-AVERAGE (lis)
    (float (/ (MY-SUM lis) (MY-LEN lis)))
)

;Problem 7
;(defun MAX-SUB-LIST (lis)
;    (if (equal lis nil)
;        0
;)

;Problem 8
(defun MYMEMBER (atm lis)
	(if (equal lis nil)
		nil
		(if (equal atm (car lis))
			atm
			(MYMEMBER atm (cdr lis))
		)
	)
)

(format t"(MAKE-SET '(1 2 3 2 3 1 4)) returns ~S~%"(MAKE-SET '(1 2 3 2 3 1 4)))
(format t"(IS-SET '(1 2 3 2 3 1 4)) returns ~S~%"(IS-SET '(1 2 3 2 3 1 4)))
(format t"(IS-SET '(1 2 3 4)) returns ~S~%"(IS-SET '(1 2 3 4)))
(format t"(MY-LEN '(1 2 3 4)) returns ~S~%"(MY-LEN '(1 2 3 4)))
(format t"(MY-LEN '()) returns ~S~%"(MY-LEN '()))
(format t"(MY-SUM '(1 2 3 4 5)) returns ~S~%"(MY-SUM '(1 2 3 4 5)))
(format t"(MY-SUM '()) returns ~S~%"(MY-SUM '()))
(format t"(MY-AVERAGE '(1 2 3 4 5)) returns ~S~%"(MY-AVERAGE '(1 2 3 4 5)))
(format t"(MY-AVERAGE '(1 2 1 2)) returns ~S~%"(MY-AVERAGE '(1 2 1 2)))

(format t"(MYMEMBER 3 '(1 2 3 4)) returns ~S~%"(MYMEMBER 3 '(1 2 3 4)))
(format t"(MYMEMBER 5 '(1 2 3 4)) returns ~S~%"(MYMEMBER 5 '(1 2 3 4)))