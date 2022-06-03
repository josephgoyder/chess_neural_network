similarity_av_parent = 0;
for a = 2:8,
    for b = 2:8,
        similarity_av_parent += similarity_nn(a, b);

    endfor
end
similarity_av_parent /= 42


similarity_av_random = 0;
for a = 1:8,
    similarity_av_random += similarity_nn(1, a);
end

similarity_av_random /= 7

