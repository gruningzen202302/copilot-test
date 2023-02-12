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