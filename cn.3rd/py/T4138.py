from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4138   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4138.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '穆拉少校',                             # 9
        '奥利维尔',                             # 10
        '达维尔大使',                           # 11
        '',                                     # 12
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02190 ._CH',             # 00
        'ED6_DT07/CH00030 ._CH',             # 01
        'ED6_DT27/CH03710 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02190P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT27/CH03710P._CP',             # 02
    )

    DeclNpc(
        X                   = 1160,
        Z                   = 4000,
        Y                   = 16920,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_13F",          # 01, 1
        "Function_2_174",          # 02, 2
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_13E")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_13E")

    Return()

    # Function_0_122 end

    def Function_1_13F(): pass

    label("Function_1_13F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157")
    OP_B1("t4138_n")
    Jump("loc_160")

    label("loc_157")

    OP_B1("t4138_y")

    label("loc_160")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173")
    OP_82(0x80, 0x0)
    OP_64(0x1, 0x1)

    label("loc_173")

    Return()

    # Function_1_13F end

    def Function_2_174(): pass

    label("Function_2_174")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(500)
    OP_1D(0x11)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05《輝く環》の事件が\x01",
            "終結してからしばらく後――\x02\x03",

            "新たな人生へと旅立って行った\x01",
            "仲間たちの後を追うように――\x02\x03",

            "ここにまた１人の青年が、\x01",
            "リベールを離れようとしていた。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 2610, 0, 72170, 225)
    SetChrPos(0x11, 1380, 0, 72520, 180)
    SetChrPos(0x12, 1430, 0, 70600, 0)
    OP_6D(3610, 0, 73730, 0)
    OP_67(0, 4450, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #1
        0x12,
        (
            "#1100Fま、まさか君が――\x02\x03",

            "――い、いや！　あなた様が\x01",
            "オリヴァルト皇子であったとは。\x02\x03",

            "ご尊顔に拝する\x01",
            "機会がなかったとはいえ、\x01",
            "数々の無礼をお許しください。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        (
            "#030F#5Pはっはっはっ。\x01",
            "そう恐縮しないでくれたまえ。\x02\x03",

            "それは身分をいつわった\x01",
            "このボクに帰すべき罪であり\x01",
            "大使には何の責任もない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12,
        (
            "#1100Fか、かたじけないお言葉――\x02\x03",

            "それにしても、ご身分を隠し\x01",
            "王国内をご遊行などとは……\x02\x03",

            "ご無事であったから良いものを\x01",
            "危うく国際問題となる所です。\x02\x03",

            "いや、お恨みしますぞ――皇子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        (
            "#030F#5Pフッ、しかしそのおかげで、\x01",
            "書物からでは決して得られぬ\x01",
            "生きた知恵を学ぶことができたわけさ。\x02\x03",

            "まあ、これからも折りに触れて\x01",
            "ちょくちょく足を運ぶ予定だから、\x01",
            "その時にはよろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x12,
        "#1100Fな、なんですと！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #6
        0x11,
        (
            "#030F#5Pどうせなら一緒に\x01",
            "温泉にでも繰り出そうじゃないか。\x02\x03",

            "フッ、共和国のエルザ大使を\x01",
            "お誘いするのも悪くはないねえ……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #7
        0x12,
        "#1100Fお、皇子……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x10,
        (
            "#270F#2Pゴホン、大使……\x02\x03",

            "いちいち真に受けていたら\x01",
            "日が暮れてしまいますよ。\x02\x03",

            "それより、先ほどお願いした\x01",
            "我々の帰国についてですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 45, 400)

    ChrTalk(    #9
        0x12,
        (
            "#1100Fあ、ああ……\x01",
            "すぐに飛行艇を手配しよう。\x02\x03",

            "外交官用の高速艇なら\x01",
            "明日には用意できると思う。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "#030F#5Pフッ、感謝するよ。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 0, 400)

    ChrTalk(    #11
        0x12,
        (
            "#1100Fいえ、皇子のお役に立つことは\x01",
            "むしろ私の喜びとするところです。\x02\x03",

            "しかも、折しも国境で\x01",
            "あのような緊張が高まった直後……\x02\x03",

            "皇子の仰る通り、\x01",
            "ここは軍用艇を用いない方が\x01",
            "懸命かも知れませんからな……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x11, 61690, 0, 10180, 90)
    SetChrPos(0x10, 59140, 0, 10300, 90)
    OP_6D(61850, 0, 11710, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #12
        0x10,
        (
            "#270F#6Pと、大使は言っていたが……\x02\x03",

            "本当のところ……\x01",
            "何を警戒しているんだ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#030F#2Pフフ、不慮の事故の可能性を\x01",
            "前もって排除しておいたまでさ。\x02\x03",

            "今回のボクの行動で\x01",
            "帝国軍主戦派の面目は丸つぶれだ。\x02\x03",

            "彼らの掌中にあっては\x01",
            "何を仕掛けて来ても不思議はない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#270F#6P事故にみせかけた謀殺――\x02\x03",

            "それもあり得るというわけか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#030F#2Pあの辛抱強い宰相殿が、\x01",
            "そこまで短気とも思えないがね。\x02\x03",

            "だが、もしボクが彼の立場なら\x01",
            "この機会を利用するかも知れない。\x02\x03",

            "――ふと、そう思ったわけさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#270F#6P……………………………\x02\x03",

            "俺の所属する第７師団は\x01",
            "お前の味方だ……\x02\x03",

            "有事の際にはすぐさま\x01",
            "行動を起こす用意はできている。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        "#030F#2Pそれは頼もしいかぎりだが……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(300)

    ChrTalk(    #18
        0x11,
        (
            "#030F#2Pしかし、我が友よ……\x01",
            "ここで下手に動いては\x01",
            "敵の思うつぼというものさ。\x02\x03",

            "街角のケンカだって\x01",
            "先に刃物を出した方が悪い。\x02\x03",

            "ボクが実力部隊に泣きついたら\x01",
            "反乱謀議そのものだからねえ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#270F#6Pそうだな……\x02\x03",

            "自衛のための根回しが過ぎて、\x01",
            "かえって追い込まれんとも限らん。\x02\x03",

            "何もしないことが、\x01",
            "最高の自衛という場合もあるか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#030F#2Pフッ、まさにその通りだよ。\x02\x03",

            "こちらの方針が判らなければ\x01",
            "敵だって対処のしようがない。\x02\x03",

            "まずは帝都に帰還し、\x01",
            "リベールで見た事件の真相を\x01",
            "皇帝陛下にご奏上する……\x02\x03",

            "その後の策は\x01",
            "出方を見てからとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    Sleep(500)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_174 end

    SaveToFile()

Try(main)
