; This is a sandbox for clojure

;make a function that prints the most repeated vaue in a series of ten values
(defn mode [a b c d e f g h i j]
  (let [count (fn [x]
                (count (filter #(= x %) [a b c d e f g h i j])))]
    (println (apply max-key count [a b c d e f g h i j]))))

;make function to print the media and the mode of ten values
(defn media-mode [a b c d e f g h i j]
  (println "Media: " (/ (+ a b c d e f g h i j) 10))
  (println "Mode: " (mode a b c d e f g h i j)))
;call the function)  
)
  
(media-mode 5 5 5 5 5 5 5 1 1 1) 

;make a function that prints the median of ten values
(defn median [a b c d e f g h i j]
  (let [sorted (sort a b c d e f g h i j)]
    (println (/ (+ (nth sorted 4) (nth sorted 5)) 2))))
;call the function
(median 5 5 5 5 5 5 5 1 1 1)

;make a function that prints a greeting according for the time of the day
(defn greeting [hour]
  (if (<= 0 hour 11)
    (println "Good morning")
    (if (<= 12 hour 17)
      (println "Good afternoon")
      (if (<= 18 hour 23)
        (println "Good evening")))))
;call the function
(greeting 12)

(greeting 23)

;make a function that outputs the current system hour
(defn system-hour []
  (let [hour (java.util.Calendar/getInstance().get(java.util.Calendar/HOUR_OF_DAY))]
    (println hour)))
;call the function
(system-hour )









