from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0113   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0113.x',
        MapIndex            = 11,
        MapDefaultBGM       = "ed60084",
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
        'Radford',                              # 9
        'Euridice',                             # 10
        'Freemont',                             # 11
        'Fate',                                 # 12
        'Yuni',                                 # 13
        'Frissa',                               # 14
        'Anya',                                 # 15
        'Mine Chief Gaton',                     # 16
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
        'ED6_DT26/CH20330 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01070 ._CH',             # 06
        'ED6_DT07/CH01530 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT26/CH20330P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01070P._CP',             # 06
        'ED6_DT07/CH01530P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 37070,
        Z                   = 0,
        Y                   = 33560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 38800,
        Z                   = 0,
        Y                   = 30060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4550,
        Z                   = 0,
        Y                   = 37480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 3140,
        Z                   = 0,
        Y                   = 32100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 3570,
        Z                   = 0,
        Y                   = 33000,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_259",          # 01, 1
        "Function_2_268",          # 02, 2
        "Function_3_3E5",          # 03, 3
        "Function_4_409",          # 04, 4
        "Function_5_480",          # 05, 5
        "Function_6_4FE",          # 06, 6
        "Function_7_6CC",          # 07, 7
        "Function_8_7F7",          # 08, 8
        "Function_9_B94",          # 09, 9
        "Function_10_D2E",         # 0A, 10
        "Function_11_E10",         # 0B, 11
        "Function_12_F03",         # 0C, 12
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_241")
    OP_4A(0x8, 255)
    SetChrPos(0x8, -41180, 0, 38000, 270)
    SetChrPos(0xA, -41280, 0, 35500, 0)
    SetChrPos(0x9, -42700, 0, 37200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x8, 6)

    label("loc_241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_258")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 11)

    label("loc_258")

    Return()

    # Function_0_1EA end

    def Function_1_259(): pass

    label("Function_1_259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_267")
    OP_6F(0x2, 15)

    label("loc_267")

    Return()

    # Function_1_259 end

    def Function_2_268(): pass

    label("Function_2_268")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3CF")

    label("loc_28D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3CF")

    label("loc_2A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3CF")

    label("loc_2BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D8")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3CF")

    label("loc_2D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F1")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3CF")

    label("loc_2F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3CF")

    label("loc_30A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_323")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3CF")

    label("loc_323")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3CF")

    label("loc_33C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_355")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3CF")

    label("loc_355")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3CF")

    label("loc_36E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3CF")

    label("loc_387")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3CF")

    label("loc_3A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3CF")

    label("loc_3B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3CF")

    label("loc_3E4")

    Return()

    # Function_2_268 end

    def Function_3_3E5(): pass

    label("Function_3_3E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_408")
    OP_8D(0xFE, -447, 33095, 4354, 30386, 4000)
    Jump("Function_3_3E5")

    label("loc_408")

    Return()

    # Function_3_3E5 end

    def Function_4_409(): pass

    label("Function_4_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418")
    Call(0, 12)
    Jump("loc_47F")

    label("loc_418")

    TalkBegin(0x9)

    ChrTalk(    #0
        0xFE,
        "That bell toll was so pretty, wasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I've never heard one chime so clearly\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_47F")

    Return()

    # Function_4_409 end

    def Function_5_480(): pass

    label("Function_5_480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F")
    Call(0, 12)
    Jump("loc_4FD")

    label("loc_48F")

    TalkBegin(0xA)

    ChrTalk(    #2
        0xFE,
        (
            "Great progress with your rounds\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "If anything happens, I promise I'll\x01",
            "contact the guild.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)

    label("loc_4FD")

    Return()

    # Function_5_480 end

    def Function_6_4FE(): pass

    label("Function_6_4FE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_6C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5B8")

    ChrTalk(    #4
        0xFE,
        (
            "I'm forbidding Yuni from going\x01",
            "outside until this fog clears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "It's my duty as a parent to keep\x01",
            "her safe, and the fog's the only\x01",
            "danger I can see right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C8")

    label("loc_5B8")


    ChrTalk(    #6
        0xFE,
        (
            "I heard there are a number of\x01",
            "people who have fallen into an\x01",
            "irreversible sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I don't know if it has anything to\x01",
            "do with this creepy fog...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Either way, I'm forbidding Yuni\x01",
            "from going outside for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "It's all I can do to keep her safe\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6C8")

    TalkEnd(0xB)
    Return()

    # Function_6_4FE end

    def Function_7_6CC(): pass

    label("Function_7_6CC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_7F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_754")

    ChrTalk(    #10
        0xFE,
        (
            "I like our house, but being locked\x01",
            "up is boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I'm gonna go outside tomorrow,\x01",
            "no matter what Papa says!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F3")

    label("loc_754")


    ChrTalk(    #12
        0xFE,
        (
            "I'm gonna do what Papa says\x01",
            "and stay in the house for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I wonder if Luke and Pat are\x01",
            "playing outside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "I wish I was! They're so lucky.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_7F3")

    TalkEnd(0xC)
    Return()

    # Function_7_6CC end

    def Function_8_7F7(): pass

    label("Function_8_7F7")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_898")

    ChrTalk(    #15
        0xF,
        (
            "We're just swamped with work.\x01",
            "I'll need to leave early tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        (
            "Well, all I can do is entrust my family\x01",
            "to Aidios while I'm away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B90")

    label("loc_898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB5")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #17
        0xF,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xF,
        (
            "Say, you're Cassius' girl, the bracer\x01",
            "who helped us before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1011FMr. Gaton! Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xF,
        (
            "Thanks to you, mining out a new\x01",
            "vein's been going just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xF,
        (
            "After what happened, we closed up\x01",
            "that hole the monsters came out of\x01",
            "with some explosives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1016FExplosives...? Umm, okay, glad to\x01",
            "hear it ended well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xF,
        (
            "Well, we intend to do some\x01",
            "construction down there later\x01",
            "and fully block that hole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xF,
        (
            "It was worth it, though. Ol' Malga's\x01",
            "running just fine now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1032)
    Jump("loc_AFC")

    label("loc_AB5")


    ChrTalk(    #25
        0xF,
        "Hey there, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xF,
        (
            "The mine's running just as fine as\x01",
            "ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFC")


    ChrTalk(    #27
        0xF,
        (
            "And, man, does she keep me busy.\x01",
            "This is my first time home in nearly\x01",
            "a week!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xF,
        (
            "Kills me that I gotta go right back\x01",
            "out there soon, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_B90")

    TalkEnd(0xF)
    Return()

    # Function_8_7F7 end

    def Function_9_B94(): pass

    label("Function_9_B94")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C3B")

    ChrTalk(    #29
        0xFE,
        (
            "My husband usually heads out to\x01",
            "the mine early in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I wish I didn't have to see him go,\x01",
            "but I suppose it's part of being married.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2A")

    label("loc_C3B")


    ChrTalk(    #31
        0xFE,
        (
            "We're having dinner tonight as a family\x01",
            "for the first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "The town may have its share of\x01",
            "problems, but happy moments like\x01",
            "these make them all feel so small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Though my husband does go back\x01",
            "to work tomorrow...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_D2A")

    TalkEnd(0xD)
    Return()

    # Function_9_B94 end

    def Function_10_D2E(): pass

    label("Function_10_D2E")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_E0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_DAC")

    ChrTalk(    #34
        0xFE,
        "So when do I feed Daddy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Daddy goes all, 'Yummy!' and it makes\x01",
            "him happy, which makes me happy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0C")

    label("loc_DAC")


    ChrTalk(    #36
        0xFE,
        (
            "I get to have dinner with Mommy and\x01",
            "Daddy tonight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Heehee! I get to feed Daddy! ☆\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_E0C")

    TalkEnd(0xE)
    Return()

    # Function_10_D2E end

    def Function_11_E10(): pass

    label("Function_11_E10")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x8, 255)
    OP_6F(0x2, 15)
    SetChrPos(0x8, -41180, 0, 38000, 270)
    SetChrPos(0xA, -41280, 0, 35500, 0)
    SetChrPos(0x9, -42700, 0, 37200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x8, 6)
    OP_6D(-39410, 0, 35550, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(-41180, 0, 38910, 3000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0134   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_11_E10 end

    def Function_12_F03(): pass

    label("Function_12_F03")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    Fade(1000)
    SetChrPos(0x101, -42370, 0, 34440, 0)
    SetChrPos(0x103, -41320, 0, 34290, 0)
    SetChrPos(0xF8, -42850, 0, 33200, 0)
    SetChrPos(0xF9, -41450, 0, 33100, 0)
    OP_8C(0xA, 180, 0)
    OP_8C(0x9, 180, 0)
    OP_6D(-41270, 0, 36170, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #38
        0xA,
        "#5POh, hello...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "#1PYou're Estelle and Scherazard, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        "#020F#4PYes, good evening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1015F#2PWe're here to investigate by order\x01",
            "of the mayor, but, uh.\x02\x03",

            "Is Mr. Radford okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "#1PYes... But there's been no change,\x01",
            "I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "#1PHe's sound asleep and SEEMS comfortable.\x01",
            "But we cannot wake him, no matter what we do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        (
            "#5PIs our only option to wait and watch\x01",
            "over him until morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x103,
        (
            "#026F#4PI'm afraid so...that's all you can do,\x01",
            "for now, at least.\x02\x03",

            "#022FI know this is a bad time, but could we\x01",
            "ask you a few questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        "#1POf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "#5PI don't know if we can answer everything,\x01",
            "but I'll be happy to help in any way I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#020F#4PThank you, you two.\x02\x03",

            "Firstly, when and where did Radford fall asleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        "#1PThe time? Around 5:30, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        "#5PThe place, well...\x02",
    )

    CloseMessageWindow()

    def lambda_12DE():
        OP_6D(-42950, 0, 34680, 1200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12DE)
    OP_8C(0xA, 230, 400)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #51
        0xA,
        "#6PJust outside that door, essentially.\x02",
    )

    CloseMessageWindow()

    def lambda_132F():
        OP_8C(0xFE, 230, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_132F)
    Sleep(50)

    def lambda_1342():
        OP_8C(0xFE, 230, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1342)
    Sleep(50)

    def lambda_1355():
        OP_8C(0xFE, 230, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1355)
    Sleep(50)

    def lambda_1368():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1368)
    Sleep(400)

    ChrTalk(    #52
        0x101,
        (
            "#1015F#6POutside the door?\x01",
            "So, what, in the hallway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#6PYes, I heard a knock, and a voice\x01",
            "say, 'I'm home!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "#6PI unlocked the door to greet him, but\x01",
            "when I did, I found my father-in-law on\x01",
            "the ground, unconscious.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_145F():
        OP_6D(-41270, 0, 36170, 1200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_145F)
    OP_8C(0xA, 180, 400)

    def lambda_147E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_147E)
    Sleep(50)

    def lambda_1491():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1491)
    Sleep(50)

    def lambda_14A4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_14A4)
    Sleep(50)

    def lambda_14B7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_14B7)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #55
        0x9,
        (
            "#1PTo be honest, I thought Father had simply\x01",
            "gotten drunk. Again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "#1PBut...I couldn't smell any alcohol on\x01",
            "his breath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "#5PI thought it was strange, and then\x01",
            "we couldn't wake him, no matter\x01",
            "what we did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        "#5PSo we went to go see Father Divine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x103,
        (
            "#026F#4PI see... I think I understand the situation.\x02\x03",

            "#022FOne last question, if I may.\x02\x03",

            "Was there anything odd about the\x01",
            "situation before Radford fell asleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "#1PAnything odd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        "#5PWhat, you mean like this blasted fog?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x103,
        (
            "#020F#4PAside from that.\x02\x03",

            "For example...did you see anyone odd,\x01",
            "hear any strange noises?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)
    Sleep(500)

    ChrTalk(    #63
        0xA,
        (
            "#2PCome...to think of it...\x01",
            "When we were dragging Radford in!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 400)
    Sleep(500)

    ChrTalk(    #64
        0x9,
        "#1PYou noticed it, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        "#1PIn all this fuss, I thought I'd just imagined it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1004F#2PEr. What is it?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #67
        0xA,
        (
            "#5PIt was when we were putting Radford\x01",
            "to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "#5PWe both heard, it seems, the sound\x01",
            "of a bell.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1937")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't heard about bell(Haven't talked to Mayor's Wife)\x01",      # 0
            "Set as have heard about bell(Have talked to Mayor's Wife)\x01",            # 1
            "No change\x01",                                                            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_192B"),
        (1, "loc_1931"),
        (SWITCH_DEFAULT, "loc_1937"),
    )


    label("loc_192B")

    OP_A3(0x1813)
    Jump("loc_1937")

    label("loc_1931")

    OP_A2(0x1813)
    Jump("loc_1937")

    label("loc_1937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199D")

    ChrTalk(    #69
        0x103,
        "#023F#4PThe sound of a bell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1004F#2PHold on a sec. Didn't...we hear one too?\x02",
    )

    CloseMessageWindow()
    Jump("loc_19DD")

    label("loc_199D")


    ChrTalk(    #71
        0x103,
        "#022F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1002F#2PThe sound of a bell here, too...\x02",
    )

    CloseMessageWindow()

    label("loc_19DD")


    ChrTalk(    #73
        0x9,
        "#1PIt was surprisingly lovely, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "#1PI simply thought someone outside rang one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x103,
        (
            "#026F#4P...Thank you. You've given us a lot\x01",
            "of information.\x02\x03",

            "#020FIf you remember anything else, please\x01",
            "contact the guild straightaway, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        "#1PYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1006F#2PWell, excuse us, then!\x02\x03",

            "We'll be back to check up tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        "#5POkay... Thank you, Estelle.\x02",
    )

    CloseMessageWindow()

    def lambda_1B60():
        OP_8C(0xA, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1B60)
    OP_8C(0x9, 90, 400)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_A2(0x1815)
    OP_28(0x90, 0x2, 0x80)
    OP_28(0x90, 0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BA2")
    OP_28(0x90, 0x1, 0x200)
    Jump("loc_1BA2")

    label("loc_1BA2")

    EventEnd(0x0)
    Return()

    # Function_12_F03 end

    SaveToFile()

Try(main)
