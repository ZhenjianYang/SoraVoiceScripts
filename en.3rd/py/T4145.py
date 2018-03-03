from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4145   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4145.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        'Erika Russell',                        # 9
        'Lt. Colonel Cid',                      # 10
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03970 ._CH',             # 00
        'ED6_DT27/CH03590 ._CH',             # 01
        'ED6_DT26/CH20373 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03970P._CP',             # 00
        'ED6_DT27/CH03590P._CP',             # 01
        'ED6_DT26/CH20373P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_134",          # 01, 1
        "Function_2_135",          # 02, 2
        "Function_3_CE0",          # 03, 3
        "Function_4_E5D",          # 04, 4
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_120")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_133")

    label("loc_120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_133")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_133")

    Return()

    # Function_0_10A end

    def Function_1_134(): pass

    label("Function_1_134")

    Return()

    # Function_1_134 end

    def Function_2_135(): pass

    label("Function_2_135")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    AddParty(0x50, 0xFF, 0xFF)
    AddParty(0x4E, 0xFF, 0xFF)
    SetChrPos(0x109, -860, 0, -5920, 270)
    SetChrPos(0x151, 810, 250, -4590, 270)
    SetChrPos(0x14F, -770, 0, -4740, 270)
    SetChrChipByIndex(0x151, 1)
    SetChrChipByIndex(0x14F, 0)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x151, 0x0, 0x0, 0x3)
    OP_43(0x14F, 0x0, 0x0, 0x3)
    OP_6D(840, 350, -4190, 0)
    OP_67(0, 7940, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(45000, 0)
    OP_6E(448, 0)

    def lambda_1E3():
        OP_6B(1970, 8000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E3)

    def lambda_1F3():
        OP_67(0, 3180, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1F3)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x10, 0x2)
    Sleep(300)

    ChrTalk(    #0
        0x109,
        (
            "#1060F#6P#100PStill, I sure didn't expect to run into little\x01",
            "Tita's mother here.\x02\x03",

            "I'd heard you and your husband were both\x01",
            "living abroad. What brought you back?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x14F,
        "Erika Russell",
        (
            "#1452F#5P#100PWhat do you think? After all that went down here,\x01",
            "there was no way I was staying out of the country\x01",
            "any longer than I had to.\x02\x03",

            "#1457FThough with how remote the region we were in is,\x01",
            "it was all over by the time word reached us.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #2
        0x14F,
        "Erika Russell",
        (
            "#1832F#5P#100PHad we found out sooner, I sure wouldn't have let\x01",
            "that maniac pull half the crap he did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        (
            "#1066F#6P#100PDoesn't sound like you're too happy with\x01",
            "the professor nowadays, huh?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #4
        0x14F,
        "Erika Russell",
        "#1455F#5P#100P#3STalk about an understatement!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #5
        0x14F,
        "Erika Russell",
        (
            "#1459F#5P#100P#2SThat whack job actually took my little girl\x01",
            "to that floating city with him!\x02\x03",

            "I get that he's soft towards her, but that's\x01",
            "no excuse for exposing her to danger!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1064F#6P#100PTh-That's fair...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x14F,
        "Erika Russell",
        (
            "#1830F#5P#100PAnd as if that isn't bad enough, he let that\x01",
            "redheaded scumbag get near her, too!\x02\x03",

            "That utter cretin isn't fit to be within fifty\x01",
            "arge of my darling Tita, never mind actually\x01",
            "getting friendly with her!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x109,
        "#1066F#6P#100PSo, uh...you don't like Agate, huh?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x14F,
        "Erika Russell",
        (
            "#1830F#5P#100PDon't you speak that filthy name in front of me\x01",
            "ever again!\x02\x03",

            "#1458FOooh, when I'm finished with him, he'll wish he'd\x01",
            "never been BORN...\x02\x03",

            "He might've survived that last onslaught, but we'll\x01",
            "see how he fares against an even more powerful\x01",
            "unit, won't we? Heheh...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_86F():
        OP_6D(1600, 500, -4140, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_86F)
    OP_8F(0x109, 0x1AE, 0xFA, 0xFFFFE8A4, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #10
        0x109,
        (
            "#1066F#4P#100P(I-I get the feeling this is a matter we're better\x01",
            "off not prying into...)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x151,
        "Lt. Colonel Cid",
        (
            "#701F#5P#100P(I thought the same, so I don't know any more\x01",
            "about it than you do.)\x02\x03",

            "(Incidentally, the Professor Russell you're more\x01",
            "familiar with is currently vacationing abroad.)\x02\x03",

            "(As such, she has been assisting us with this \x01",
            "case in his place.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1060F#4P#100P(Oh, I see...)\x02",
    )

    CloseMessageWindow()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_72(0x803, 0x0)
    ExitThread()
    OP_44(0x14F, 0x0)
    SetChrSubChip(0x14F, 0)
    OP_8C(0x14F, 90, 600)
    OP_44(0x109, 0x0)
    SetChrSubChip(0x109, 0)
    OP_44(0x151, 0x0)
    SetChrSubChip(0x151, 0)

    NpcTalk(    #13
        0x14F,
        "Erika Russell",
        "#1830F#3S#6P#100PAre you two listening to me?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        "#1064F#4P#100PS-Sorry!\x02",
    )


    NpcTalk(    #15
        0x151,
        "Lt. Colonel Cid",
        "#702F#5P#100PO-Of course!\x02",
    )

    OP_56(0x1)
    OP_59()
    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #16
        0x14F,
        "Erika Russell",
        "#1832F#6P#100PHmph. Well, whatever.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14F, 270, 400)

    def lambda_B56():
        OP_6D(840, 350, -4190, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B56)

    def lambda_B6E():
        OP_8F(0xFE, 0xFFFFF8A8, 0xFFFFFF06, 0xFFFFEE08, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 0, lambda_B6E)
    Sleep(100)

    def lambda_B8E():
        OP_8F(0xFE, 0xFFFFFCA4, 0x0, 0xFFFFE8E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B8E)
    Sleep(200)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x151, 0x0, 0x0, 0x3)
    OP_43(0x14F, 0x0, 0x0, 0x3)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_71(0x800, 0x0)
    ExitThread()
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_71(0x801, 0x0)
    ExitThread()
    OP_71(0x2003, 0x0)
    ExitThread()
    OP_71(0x803, 0x0)
    ExitThread()
    Sleep(3000)

    NpcTalk(    #17
        0x14F,
        "Erika Russell",
        (
            "#1452F#5P#100PThis staircase sure is long, though.\x02\x03",

            "How much farther do we have to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        "#1060F#2P#100PNot much, as far as I know.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(    #19
        0x109,
        "#1062F#2P#100PYup. There we go.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x50, 0xFF)
    RemoveParty(0x4E, 0xFF)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4145   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_135 end

    def Function_3_CE0(): pass

    label("Function_3_CE0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D05")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_E47")

    label("loc_D05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_E47")

    label("loc_D1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D37")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_E47")

    label("loc_D37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D50")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_E47")

    label("loc_D50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D69")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_E47")

    label("loc_D69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D82")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_E47")

    label("loc_D82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_E47")

    label("loc_D9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB4")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_E47")

    label("loc_DB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCD")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_E47")

    label("loc_DCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE6")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_E47")

    label("loc_DE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_E47")

    label("loc_DFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E18")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_E47")

    label("loc_E18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E31")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_E47")

    label("loc_E31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E47")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_E47")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E5C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_E47")

    label("loc_E5C")

    Return()

    # Function_3_CE0 end

    def Function_4_E5D(): pass

    label("Function_4_E5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x109, -79990, 0, -3600, 0)
    SetChrPos(0x11, -79300, 0, -6300, 0)
    SetChrPos(0x10, -80660, 0, -5340, 0)
    OP_6D(-77590, 500, -15350, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(359, 0)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_72(0x803, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_71(0x404, 0x0)
    ExitThread()
    LoadEffect(0x0, "map\\mp082_00.eff")
    LoadEffect(0x1, "scraft\\sc008_02.eff")
    LoadEffect(0x2, "map\\mp259_02.eff")
    LoadEffect(0x3, "map\\mpP90_00.eff")
    LoadEffect(0x4, "map\\mpP90_01.eff")
    LoadEffect(0x5, "map\\mpP90_04.eff")

    def lambda_F88():
        OP_8E(0xFE, 0xFFFEC758, 0x0, 0x4C68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F88)
    Sleep(50)

    def lambda_FA8():
        OP_8E(0xFE, 0xFFFECA00, 0x0, 0x4466, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_FA8)
    Sleep(50)

    def lambda_FC8():
        OP_8E(0xFE, 0xFFFEC4EC, 0x0, 0x448E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_FC8)

    def lambda_FE3():
        OP_6D(-77890, 500, 21500, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FE3)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(-78410, 0, 20750, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(322, 0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)
    Sleep(300)

    ChrTalk(    #20
        0x11,
        "#702FA dead end?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#1459F#6PI hope you've got a good explanation for this.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #22
        0x109,
        (
            "#1065F#5PI do.\x02\x03",

            "#1063FThis isn't a dead end, but to go any farther,\x01",
            "I'm going to need you to undertake a ritual\x01",
            "of sorts for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        "#700FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1452F#6PWell, this certainly took a turn for the\x01",
            "strange.\x02\x03",

            "Is this an example of the church's famous\x01",
            "Thaumaturgy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1075F#5PSomething like that, yes.\x02\x03",

            "#1060FSpecifically, I would like you to undertake\x01",
            "a form of suggestion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        "#702FI'm...not sure I follow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#1459F#6PYou want us to promise not to tell anyone\x01",
            "what we see here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1060F#5PThat's a little extreme, so no. The colonel is\x01",
            "obviously going to need to report what\x01",
            "happened here to his superiors, for one thing.\x02\x03",

            "#1075FAll I want you to promise is that you won't tell\x01",
            "anyone who you aren't certain you can trust.\x02\x03",

            "#1066FI don't need you to say it. I just need you to\x01",
            "think and believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#1457F#6PWeird, but all right.\x02\x03",

            "#1456FIf that's all you want us to do, so be it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#701FI feel the same way.\x02\x03",

            "Should we deliberately repeat it in our minds,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1060F#5PYou don't even need to do that. It should just\x01",
            "come completely naturally to you.\x02\x03",

            "#1075FAll right, here goes...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    Sleep(500)

    ChrTalk(    #32
        0x109,
        (
            "#1063F#5PIn the name of She Who Dwells Above do I hold\x01",
            "this consecrated septium.\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x0, 0x109, -150, 800, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #33
        0x109,
        (
            "#1065F#5PSpace's golden glow... Consciousness' silver glow...\x02\x03",

            "By your opposing natures, reveal to them the path\x01",
            "that leads to your sacrament!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -80040, 1000, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC9)
    OP_82(0x0, 0x2)
    Sleep(2000)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0x10, 0, 800, 0, 0, 0, 0, 1400, 2400, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, 0, 800, 0, 0, 0, 0, 1400, 2400, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()

    ChrTalk(    #34
        0x10,
        "#1454F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        "#702FHmm?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-78920, 500, 22990, 0)
    OP_67(0, 4260, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(33000, 0)
    OP_6E(330, 0)
    OP_22(0xD7, 0x0, 0x64)
    OP_22(0x146, 0x64, 0x1)
    PlayEffect(0x3, 0x7, 0xFF, -80000, 0, 21950, 0, 0, 0, 2300, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0xFF, -80000, 0, 21950, 0, 0, 0, 2300, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x5, 0xFF, -80000, 0, 21950, 0, 0, 0, 2300, 1600, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)

    def lambda_1848():
        OP_6B(2640, 800)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1848)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    OP_82(0x5, 0x0)
    OP_0D()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x10,
        "#1455F#6PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        "#702FHow did that door appear?!\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_0D()

    def lambda_18F2():
        OP_6D(-78410, 0, 20750, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18F2)

    def lambda_190A():
        OP_67(0, 4860, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_190A)

    def lambda_1922():
        OP_6B(2550, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1922)

    def lambda_1932():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1932)

    def lambda_1942():
        OP_6E(322, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1942)
    WaitChrThread(0x109, 0x0)
    SetChrSubChip(0x109, 0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    Sleep(500)

    ChrTalk(    #38
        0x109,
        (
            "#1075F#5PThank you both for your assistance.\x02\x03",

            "#1060FI can see that you were true to your\x01",
            "word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#1457F#6P...Ahh, I see.\x02\x03",

            "#1459FSo if we just said it but didn't really mean it,\x01",
            "we wouldn't be able to see anything, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#703FAnd yet I can hardly believe what happened...\x02\x03",

            "#700FI imagine it would be uncouth of me to ask\x01",
            "how all of this works?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x109,
        "#1066F#5PYeeeah, I'd really rather you didn't.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x10, 0x4)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    def lambda_1B2E():
        OP_6D(-78410, 0, 21400, 1200)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B2E)
    OP_8E(0x109, 0xFFFEC6FE, 0x0, 0x5398, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x70, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x10E)
    OP_73(0x3)
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #42
        0x109,
        "#1060F#5PAnyway, come on in.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    def lambda_1BAA():
        OP_6D(-77850, 0, 23770, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1BAA)

    def lambda_1BC2():
        OP_8E(0xFE, 0xFFFEC802, 0x0, 0x5FAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BC2)
    Sleep(150)

    def lambda_1BE2():
        OP_8E(0xFE, 0xFFFEC4EC, 0x0, 0x5FAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1BE2)
    Sleep(300)

    def lambda_1C02():
        OP_8E(0xFE, 0xFFFECA00, 0x0, 0x5FAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1C02)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4144   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_4_E5D end

    SaveToFile()

Try(main)
