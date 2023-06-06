var w = function(e, t) {
    return e << t | e >>> 32 - t
}
A = function(e, t, n, r, i, a, o) {
    return e = P(e, P(P(function(e, t, n) {
        return e & n | t & ~n
    }(t, n, r), i), o)),
    P(w(e, a), t)
}
E = function(e, t, n, r, i, a, o) {
    return e = P(e, P(P(function(e, t, n) {
        return e ^ t ^ n
    }(t, n, r), i), o)),
    P(w(e, a), t)
}
P = function(e, t) {
    var n, r, i, a, o;
    return i = 2147483648 & e,
    a = 2147483648 & t,
    o = (1073741823 & e) + (1073741823 & t),
    (n = 1073741824 & e) & (r = 1073741824 & t) ? 2147483648 ^ o ^ i ^ a : n | r ? 1073741824 & o ? 3221225472 ^ o ^ i ^ a : 1073741824 ^ o ^ i ^ a : o ^ i ^ a
}
D = function(e, t, n, r, i, a, o) {
    return e = P(e, P(P(function(e, t, n) {
        return t ^ (e | ~n)
    }(t, n, r), i), o)),
    P(w(e, a), t)
}
L = function(e) {
    var t, n = "", r = "";
    for (t = 0; t <= 3; t++)
        n += (r = "0" + (e >>> 8 * t & 255).toString(16)).substr(r.length - 2, 2);
    return n
}
I = function(e, t, n, r, i, a, o) {
    return e = P(e, P(P(function(e, t, n) {
        return e & t | ~e & n
    }(t, n, r), i), o)),
    P(w(e, a), t)
}
function R(e) {
    e += "";
    var t, n, r, i, a, o, s, u, c, l = Array();
    for (e = function(e) {
        e = e.replace(/\x0d\x0a/g, "\n");
        for (var t = "", n = 0; n < e.length; n++) {
            var r = e.charCodeAt(n);
            r < 128 ? t += String.fromCharCode(r) : r > 127 && r < 2048 ? (t += String.fromCharCode(r >> 6 | 192),
            t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
            t += String.fromCharCode(r >> 6 & 63 | 128),
            t += String.fromCharCode(63 & r | 128))
        }
        return t
    }(e),
    l = function(e) {
        for (var t, n = e.length, r = n + 8, i = 16 * ((r - r % 64) / 64 + 1), a = Array(i - 1), o = 0, s = 0; s < n; )
            o = s % 4 * 8,
            a[t = (s - s % 4) / 4] = a[t] | e.charCodeAt(s) << o,
            s++;
        return o = s % 4 * 8,
        a[t = (s - s % 4) / 4] = a[t] | 128 << o,
        a[i - 2] = n << 3,
        a[i - 1] = n >>> 29,
        a
    }(e),
    o = 1732584193,
    s = 4023233417,
    u = 2562383102,
    c = 271733878,
    t = 0; t < l.length; t += 16)
        n = o,
        r = s,
        i = u,
        a = c,
        o = I(o, s, u, c, l[t + 0], 7, 3614090360),
        c = I(c, o, s, u, l[t + 1], 12, 3905402710),
        u = I(u, c, o, s, l[t + 2], 17, 606105819),
        s = I(s, u, c, o, l[t + 3], 22, 3250441966),
        o = I(o, s, u, c, l[t + 4], 7, 4118548399),
        c = I(c, o, s, u, l[t + 5], 12, 1200080426),
        u = I(u, c, o, s, l[t + 6], 17, 2821735955),
        s = I(s, u, c, o, l[t + 7], 22, 4249261313),
        o = I(o, s, u, c, l[t + 8], 7, 1770035416),
        c = I(c, o, s, u, l[t + 9], 12, 2336552879),
        u = I(u, c, o, s, l[t + 10], 17, 4294925233),
        s = I(s, u, c, o, l[t + 11], 22, 2304563134),
        o = I(o, s, u, c, l[t + 12], 7, 1804603682),
        c = I(c, o, s, u, l[t + 13], 12, 4254626195),
        u = I(u, c, o, s, l[t + 14], 17, 2792965006),
        s = I(s, u, c, o, l[t + 15], 22, 1236535329),
        o = A(o, s, u, c, l[t + 1], 5, 4129170786),
        c = A(c, o, s, u, l[t + 6], 9, 3225465664),
        u = A(u, c, o, s, l[t + 11], 14, 643717713),
        s = A(s, u, c, o, l[t + 0], 20, 3921069994),
        o = A(o, s, u, c, l[t + 5], 5, 3593408605),
        c = A(c, o, s, u, l[t + 10], 9, 38016083),
        u = A(u, c, o, s, l[t + 15], 14, 3634488961),
        s = A(s, u, c, o, l[t + 4], 20, 3889429448),
        o = A(o, s, u, c, l[t + 9], 5, 568446438),
        c = A(c, o, s, u, l[t + 14], 9, 3275163606),
        u = A(u, c, o, s, l[t + 3], 14, 4107603335),
        s = A(s, u, c, o, l[t + 8], 20, 1163531501),
        o = A(o, s, u, c, l[t + 13], 5, 2850285829),
        c = A(c, o, s, u, l[t + 2], 9, 4243563512),
        u = A(u, c, o, s, l[t + 7], 14, 1735328473),
        s = A(s, u, c, o, l[t + 12], 20, 2368359562),
        o = E(o, s, u, c, l[t + 5], 4, 4294588738),
        c = E(c, o, s, u, l[t + 8], 11, 2272392833),
        u = E(u, c, o, s, l[t + 11], 16, 1839030562),
        s = E(s, u, c, o, l[t + 14], 23, 4259657740),
        o = E(o, s, u, c, l[t + 1], 4, 2763975236),
        c = E(c, o, s, u, l[t + 4], 11, 1272893353),
        u = E(u, c, o, s, l[t + 7], 16, 4139469664),
        s = E(s, u, c, o, l[t + 10], 23, 3200236656),
        o = E(o, s, u, c, l[t + 13], 4, 681279174),
        c = E(c, o, s, u, l[t + 0], 11, 3936430074),
        u = E(u, c, o, s, l[t + 3], 16, 3572445317),
        s = E(s, u, c, o, l[t + 6], 23, 76029189),
        o = E(o, s, u, c, l[t + 9], 4, 3654602809),
        c = E(c, o, s, u, l[t + 12], 11, 3873151461),
        u = E(u, c, o, s, l[t + 15], 16, 530742520),
        s = E(s, u, c, o, l[t + 2], 23, 3299628645),
        o = D(o, s, u, c, l[t + 0], 6, 4096336452),
        c = D(c, o, s, u, l[t + 7], 10, 1126891415),
        u = D(u, c, o, s, l[t + 14], 15, 2878612391),
        s = D(s, u, c, o, l[t + 5], 21, 4237533241),
        o = D(o, s, u, c, l[t + 12], 6, 1700485571),
        c = D(c, o, s, u, l[t + 3], 10, 2399980690),
        u = D(u, c, o, s, l[t + 10], 15, 4293915773),
        s = D(s, u, c, o, l[t + 1], 21, 2240044497),
        o = D(o, s, u, c, l[t + 8], 6, 1873313359),
        c = D(c, o, s, u, l[t + 15], 10, 4264355552),
        u = D(u, c, o, s, l[t + 6], 15, 2734768916),
        s = D(s, u, c, o, l[t + 13], 21, 1309151649),
        o = D(o, s, u, c, l[t + 4], 6, 4149444226),
        c = D(c, o, s, u, l[t + 11], 10, 3174756917),
        u = D(u, c, o, s, l[t + 2], 15, 718787259),
        s = D(s, u, c, o, l[t + 9], 21, 3951481745),
        o = P(o, n),
        s = P(s, r),
        u = P(u, i),
        c = P(c, a);
    return (L(o) + L(s) + L(u) + L(c)).toLowerCase()
}

function main(tvid, tm) {
    res = Object(R)(Object(R)("") + tvid + "" + tm);
    return res;
}
