from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1400   ._SN',
        MapName             = 'Bose',
        Location            = 'C1400.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60022",
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
        'Whemler',                              # 9
        'Agate',                                # 10
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
        'ED6_DT07/CH01680 ._CH',             # 00
        'ED6_DT06/CH20053 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01680P._CP',             # 00
        'ED6_DT06/CH20053P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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


    DeclEvent(
        X                   = -59360,
        Y                   = 2000,
        Z                   = 181540,
        Range               = -67440,
        Unknown_10          = 0x1F40,
        Unknown_14          = 0x2B390,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_163",          # 01, 1
        "Function_2_186",          # 02, 2
        "Function_3_19C",          # 03, 3
        "Function_4_4DF",          # 04, 4
        "Function_5_A01",          # 05, 5
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 0)), scpexpr(EXPR_END)), "loc_143")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -60800, 3970, 187600, 270)

    label("loc_143")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_162")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_162")

    Return()

    # Function_0_11A end

    def Function_1_163(): pass

    label("Function_1_163")

    OP_72(0x401, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_185")

    Return()

    # Function_1_163 end

    def Function_2_186(): pass

    label("Function_2_186")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_186")

    label("loc_19B")

    Return()

    # Function_2_186 end

    def Function_3_19C(): pass

    label("Function_3_19C")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "Hmm? Somethin' I can help you with?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Rest\x01",            # 0
            "Share Food\x01",      # 1
            "Cancel\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x10, 0xFE, 0x0)
    OP_31(0x11, 0xFE, 0x0)
    OP_31(0x12, 0xFE, 0x0)
    Sleep(1000)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #1
        0xFE,
        "Enjoy your break?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Good luck in there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DB")

    label("loc_291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A6")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #3
        "\x06\x07\x00Ate \x07\x02Abaddon Potluck\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_31A"),
        (1, "loc_35B"),
        (2, "loc_39C"),
        (SWITCH_DEFAULT, "loc_3DD"),
    )


    label("loc_31A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_332")
    OP_31(0x10, 0x2, 0x1)
    OP_31(0x10, 0x5, 0x0)

    label("loc_332")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_345")
    OP_31(0x11, 0x5, 0x64)

    label("loc_345")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_358")
    OP_31(0x12, 0x5, 0x64)

    label("loc_358")

    Jump("loc_3DD")

    label("loc_35B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E")
    OP_31(0x10, 0x5, 0x64)

    label("loc_36E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_386")
    OP_31(0x11, 0x2, 0x1)
    OP_31(0x11, 0x5, 0x0)

    label("loc_386")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_399")
    OP_31(0x12, 0x5, 0x64)

    label("loc_399")

    Jump("loc_3DD")

    label("loc_39C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AF")
    OP_31(0x10, 0x5, 0x64)

    label("loc_3AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C2")
    OP_31(0x11, 0x5, 0x64)

    label("loc_3C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DA")
    OP_31(0x12, 0x2, 0x1)
    OP_31(0x12, 0x5, 0x0)

    label("loc_3DA")

    Jump("loc_3DD")

    label("loc_3DD")

    Jump("loc_463")

    label("loc_3E0")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_407"),
        (1, "loc_435"),
        (SWITCH_DEFAULT, "loc_463"),
    )


    label("loc_407")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41F")
    OP_31(0x10, 0x2, 0x1)
    OP_31(0x10, 0x5, 0x0)

    label("loc_41F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_432")
    OP_31(0x11, 0x5, 0x64)

    label("loc_432")

    Jump("loc_463")

    label("loc_435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x10)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_448")
    OP_31(0x10, 0x5, 0x64)

    label("loc_448")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x11)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_460")
    OP_31(0x11, 0x2, 0x1)
    OP_31(0x11, 0x5, 0x0)

    label("loc_460")

    Jump("loc_463")

    label("loc_463")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #4
        0xFE,
        "Well? Feeling full now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Good luck in there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DB")

    label("loc_4A6")


    ChrTalk(    #6
        0xFE,
        "No need for help, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Good luck in there!\x02",
    )

    CloseMessageWindow()

    label("loc_4DB")

    TalkEnd(0xFE)
    Return()

    # Function_3_19C end

    def Function_4_4DF(): pass

    label("Function_4_4DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-62140, 3940, 188700, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(3380, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -63680, 3950, 188120, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -62400, 3950, 188260, 180)
    OP_4A(0x10, 255)
    SetChrPos(0x113, -64780, 4070, 185560, 0)
    SetChrPos(0x111, -63880, 4070, 185560, 0)
    SetChrPos(0x112, -62980, 4070, 185560, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x11,
        "#051F#5PThis here's the entrance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x111,
        (
            "#1743F#12PNever would've thought there was a\x01",
            "cave way out here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x112,
        (
            "#1750F#12PHeh. So this is the place that's gonna\x01",
            "determine our futures, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x113,
        "#1765F#6PIt's sure hidden well enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#053F#5PWell, you already know what you're doing.\x02\x03",

            "#051FI'll be waiting for you at the end, so give it\x01",
            "your best shot.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 500)
    Sleep(200)

    def lambda_714():
        OP_8E(0xFE, 0xFFFF0740, 0xFAA, 0x2EB80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_714)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)

    ChrTalk(    #13
        0x10,
        "#5PI'll be here backing you up if you need it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#5PIf things get too dicey and you need a\x01",
            "break or something to eat, come to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x113,
        (
            "#1761F#6PSounds like an easy enough job for you.\x01",
            "As if we'll even need to come back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x112,
        (
            "#1751F#12PYeah! We'll breeze through this thing in\x01",
            "no time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        "#5P...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x10, 90, 500)

    def lambda_877():
        OP_8E(0xFE, 0xFFFF1280, 0xF82, 0x2DCD0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_877)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 270, 500)
    Sleep(300)

    ChrTalk(    #18
        0x111,
        "#1741F#12PAll right, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x112,
        "#1750F#12PI'm ready if you guys are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x113,
        "#1761F#6PTime to get to work.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F90)
    OP_C2(0x1, 0x4)
    OP_31(0x10, 0x10, 0x2D)
    OP_31(0x10, 0xFE, 0x0)
    OP_31(0x10, 0x5, 0x0)
    OP_35(0x10, 0xFFFF)
    OP_34(0x10, 0xFFFF)
    OP_35(0x10, 0x0)
    OP_BB(0x10, 0x6, 0x0)
    OP_41(0x10, 0x0, 0xFF)
    OP_41(0x10, 0x605, 0xFF)
    OP_41(0x10, 0x640, 0xFF)
    OP_41(0x10, 0x80, 0xFF)
    OP_31(0x11, 0x10, 0x2D)
    OP_31(0x11, 0xFE, 0x0)
    OP_31(0x11, 0x5, 0x0)
    OP_35(0x11, 0xFFFF)
    OP_34(0x11, 0xFFFF)
    OP_35(0x11, 0x0)
    OP_BB(0x11, 0x6, 0x0)
    OP_41(0x11, 0x0, 0xFF)
    OP_41(0x11, 0x605, 0xFF)
    OP_41(0x11, 0x640, 0xFF)
    OP_41(0x11, 0x80, 0xFF)
    OP_31(0x12, 0x10, 0x2D)
    OP_31(0x12, 0xFE, 0x0)
    OP_31(0x12, 0x5, 0x0)
    OP_35(0x12, 0xFFFF)
    OP_34(0x12, 0xFFFF)
    OP_35(0x12, 0x0)
    OP_BB(0x12, 0x6, 0x0)
    OP_41(0x12, 0x0, 0xFF)
    OP_41(0x12, 0x605, 0xFF)
    OP_41(0x12, 0x640, 0xFF)
    OP_41(0x12, 0x80, 0xFF)
    OP_3E(0x1D6, 3)
    OP_3E(0x1D7, 2)
    OP_3E(0x1D8, 2)
    OP_3E(0x1D9, 4)
    OP_3E(0x1DA, 2)
    OP_3E(0x13E, 1)
    OP_3E(0x1F0, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E9")
    OP_3E(0x160, 1)
    Jump("loc_9FA")

    label("loc_9E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FA")
    OP_3E(0x160, 1)

    label("loc_9FA")

    EventEnd(0x0)
    OP_4B(0x10, 255)
    Return()

    # Function_4_4DF end

    def Function_5_A01(): pass

    label("Function_5_A01")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AB4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A46")

    ChrTalk(    #21
        0x111,
        "#1740F*sigh* Time to get back in there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB1")

    label("loc_A46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7B")

    ChrTalk(    #22
        0x112,
        "#1750FTime to get back in there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB1")

    label("loc_A7B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB1")

    ChrTalk(    #23
        0x113,
        "#1763FHmph. Let's get back in there.\x02",
    )

    CloseMessageWindow()

    label("loc_AB1")

    Jump("loc_E8C")

    label("loc_AB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x12)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD7")
    OP_4A(0x10, 255)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B59")

    ChrTalk(    #24
        0x10,
        "#6PHuh? You throwing in the towel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#6PNo shame in that. Sometimes it's important\x01",
            "to know when to give up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C53")

    label("loc_B59")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE5")

    ChrTalk(    #26
        0x10,
        "#6PHuh? You throwing in the towel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#6PNo shame in that. Sometimes it's important\x01",
            "to know when to give up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C53")

    label("loc_BE5")


    ChrTalk(    #28
        0x10,
        "Huh? You throwing in the towel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "No shame in that. Sometimes it's important\x01",
            "to know when to give up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C53")


    ChrTalk(    #30
        0x111,
        "#1741FBah... Not a chance in hell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x113,
        "#1763FWe ain't giving up. No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x112,
        "#1756FLet's get back in there.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_8C(0x10, 270, 0)
    OP_4B(0x10, 255)
    Jump("loc_E8C")

    label("loc_CD7")

    OP_4A(0x10, 255)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D60")

    ChrTalk(    #33
        0x10,
        "#6PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "#6PYou two seriously planning on giving up and\x01",
            "just leaving your friend in there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3E")

    label("loc_D60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDE")

    ChrTalk(    #35
        0x10,
        "#6PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "#6PYou two seriously planning on giving up and\x01",
            "just leaving your friend in there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3E")

    label("loc_DDE")


    ChrTalk(    #37
        0x10,
        "Wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "You two seriously planning on giving up and\x01",
            "just leaving your friend in there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3E")


    ChrTalk(    #39
        0x111,
        "#1744FHeh. 'Fraid not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x112,
        "#1750FWe ain't THAT heartless.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_8C(0x10, 270, 0)
    OP_4B(0x10, 255)

    label("loc_E8C")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_5_A01 end

    SaveToFile()

Try(main)
