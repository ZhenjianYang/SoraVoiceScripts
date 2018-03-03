from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1110   ._SN',
        MapName             = 'Bose',
        Location            = 'T1110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Modena',                               # 9
        'Trino',                                # 10
        'Anelace',                              # 11
        'Target Camera',                        # 12
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01680 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01480 ._CH',             # 04
        'ED6_DT07/CH01220 ._CH',             # 05
        'ED6_DT07/CH01010 ._CH',             # 06
        'ED6_DT07/CH01000 ._CH',             # 07
        'ED6_DT07/CH01183 ._CH',             # 08
        'ED6_DT07/CH01230 ._CH',             # 09
        'ED6_DT07/CH01200 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01143 ._CH',             # 0C
        'ED6_DT27/CH03090 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01680P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01480P._CP',             # 04
        'ED6_DT07/CH01220P._CP',             # 05
        'ED6_DT07/CH01010P._CP',             # 06
        'ED6_DT07/CH01000P._CP',             # 07
        'ED6_DT07/CH01183P._CP',             # 08
        'ED6_DT07/CH01230P._CP',             # 09
        'ED6_DT07/CH01200P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01143P._CP',             # 0C
        'ED6_DT27/CH03090P._CP',             # 0D
    )

    DeclNpc(
        X                   = -18730,
        Z                   = 70,
        Y                   = 33060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -21100,
        Z                   = 0,
        Y                   = 33600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1C3",          # 01, 1
        "Function_2_1C4",          # 02, 2
        "Function_3_1C9",          # 03, 3
        "Function_4_1ED",          # 04, 4
        "Function_5_211",          # 05, 5
        "Function_6_2AE",          # 06, 6
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1C2")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_1C2")

    Return()

    # Function_0_19A end

    def Function_1_1C3(): pass

    label("Function_1_1C3")

    Return()

    # Function_1_1C3 end

    def Function_2_1C4(): pass

    label("Function_2_1C4")

    Call(6, 2)
    Return()

    # Function_2_1C4 end

    def Function_3_1C9(): pass

    label("Function_3_1C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EC")
    OP_8D(0xFE, 26200, 71400, 28400, 72600, 2000)
    Jump("Function_3_1C9")

    label("loc_1EC")

    Return()

    # Function_3_1C9 end

    def Function_4_1ED(): pass

    label("Function_4_1ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_210")
    OP_8D(0xFE, 17430, 68790, 23880, 64870, 1500)
    Jump("Function_4_1ED")

    label("loc_210")

    Return()

    # Function_4_1ED end

    def Function_5_211(): pass

    label("Function_5_211")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2AD")
    OP_8E(0xFE, 0xFFFFA6F0, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFAB8C, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFADE4, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAEC0, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFADE4, 0x0, 0x11C60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAB8C, 0x0, 0x11B34, 0x7D0, 0x0)
    Jump("Function_5_211")

    label("loc_2AD")

    Return()

    # Function_5_211 end

    def Function_6_2AE(): pass

    label("Function_6_2AE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-19160, 0, 34000, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -20640, 0, 31700, 0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#A
        "\x07\x00#4S#15ATestimony 3\x18\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x10,
        (
            "#11PYou want to ask about a man who's been\x01",
            "spending time with Lila lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#11PHmm... Thinking back, I did see her with a man\x01",
            "when my husband and I went to the market...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "#11PThey were looking at souvenirs together, I believe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        "#5PHaha. I remember it well, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x11,
        "#5PI've rarely seen a more adoring pair in my life.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        "#5PThey were like a pair of newlyweds.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        "#814F#12PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "#11PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#11PI wouldn't pay much attention to anything my\x01",
            "husband says. He has a habit of exaggerating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#5PHaha. I'm not ashamed of it, either! These kinds\x01",
            "of stories are always much more interesting with\x01",
            "a touch of dramatic flair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        "#819F#12PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#11PIt wasn't the first time I've seen the man,\x01",
            "though. I'm sure I've met him before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#11PBut I can't for the life of me remember his name...\x01",
            "Can you remember, dear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#5PDon't be silly. Of course I remember!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#5PI would never forget the name of a man\x01",
            "I've done good business with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        "#5PThat was young Lenard.\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #17
        0x12,
        (
            "#814F#12PWait. I know that name...\x02\x03",

            "#1310FLenard from the Kingfisher Inn?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#5P...Oh, you know him already?\x01",
            "Well, that puts a damper on my fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12,
        (
            "#819F#12PI use that place a lot for work reasons,\x01",
            "so I even know him by face.\x02\x03",

            "#816FI can't say I know all that much about him\x01",
            "as a person, though...\x02\x03",

            "If you're well acquainted with him, would\x01",
            "you tell me a bit more about him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#5PI don't mind...but this information isn't\x01",
            "going to come cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        "#1317F#12P#3SYou're gonna charge me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        "#11PPlease! That's not funny, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#11PWe owe ever so much to the Bracer Guild!\x01",
            "You can't threaten to charge a member.\x01",
            "I won't have it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#5PSorry, but I just can't help myself to a good\x01",
            "joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x12,
        "#819F#12PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "#5PLet's see... Well, he's a good, honest man for\x01",
            "starters...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)

    def lambda_AAB():
        OP_6B(3120, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AAB)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    SetMapFlags(0x2000000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_2AE end

    SaveToFile()

Try(main)
