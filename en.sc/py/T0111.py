from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0111   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0111.x',
        MapIndex            = 11,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0111_1 ._SN',
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
        'ED6_DT07/CH01000 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01070 ._CH',             # 06
        'ED6_DT07/CH01530 ._CH',             # 07
        'ED6_DT26/CH20330 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01070P._CP',             # 06
        'ED6_DT07/CH01530P._CP',             # 07
        'ED6_DT26/CH20330P._CP',             # 08
    )

    DeclNpc(
        X                   = -35400,
        Z                   = 0,
        Y                   = 36030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -39940,
        Z                   = 0,
        Y                   = 33130,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -42500,
        Z                   = 0,
        Y                   = 37200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4600,
        Z                   = 0,
        Y                   = 31530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_326",          # 01, 1
        "Function_2_35D",          # 02, 2
        "Function_3_4DA",          # 03, 3
        "Function_4_4FE",          # 04, 4
        "Function_5_16A9",         # 05, 5
        "Function_6_1C8F",         # 06, 6
        "Function_7_22F6",         # 07, 7
        "Function_8_25B1",         # 08, 8
        "Function_9_2FB1",         # 09, 9
        "Function_10_3653",        # 0A, 10
        "Function_11_41E8",        # 0B, 11
        "Function_12_4737",        # 0C, 12
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_24D")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -39720, 0, 35090, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, 5460, 0, 34000, 90)
    SetChrPos(0xE, 2390, 0, 31560, 51)
    OP_43(0xE, 0x0, 0x0, 0x2)

    label("loc_24A")

    Jump("loc_306")

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_28C")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, 37990, 0, 33540, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_279")
    SetChrFlags(0xF, 0x80)

    label("loc_279")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289")
    SetChrFlags(0xF, 0x10)

    label("loc_289")

    Jump("loc_306")

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2BA")
    SetChrPos(0x8, -41180, 0, 38000, 270)
    OP_4A(0x8, 255)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_306")

    label("loc_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2F2")
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x8, -41180, 0, 38000, 270)
    OP_4A(0x8, 255)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_306")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_306")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_306")

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_317")
    OP_A3(0x10F0)
    Event(0, 12)
    Jump("loc_325")

    label("loc_317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_325")
    OP_A3(0x10F1)
    Event(1, 3)

    label("loc_325")

    Return()

    # Function_0_1F2 end

    def Function_1_326(): pass

    label("Function_1_326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_330")
    Jump("loc_35C")

    label("loc_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x2, 15)
    Jump("loc_35C")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_352")
    OP_6F(0x2, 15)
    Jump("loc_35C")

    label("loc_352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_35C")
    Jump("loc_35C")

    label("loc_35C")

    Return()

    # Function_1_326 end

    def Function_2_35D(): pass

    label("Function_2_35D")

    RunExpression(0xE, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4C4")

    label("loc_382")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4C4")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4C4")

    label("loc_3B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4C4")

    label("loc_3CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4C4")

    label("loc_3E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4C4")

    label("loc_3FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_418")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4C4")

    label("loc_418")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4C4")

    label("loc_431")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4C4")

    label("loc_44A")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4C4")

    label("loc_463")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4C4")

    label("loc_47C")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4C4")

    label("loc_495")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4C4")

    label("loc_4AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C4")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4C4")

    label("loc_4D9")

    Return()

    # Function_2_35D end

    def Function_3_4DA(): pass

    label("Function_3_4DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FD")
    OP_8D(0xFE, -447, 33095, 4354, 30386, 4000)
    Jump("Function_3_4DA")

    label("loc_4FD")

    Return()

    # Function_3_4DA end

    def Function_4_4FE(): pass

    label("Function_4_4FE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E4")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x102, 0)
    Sleep(1000)

    ChrTalk(    #0
        0xFE,
        "Ah, Estelle...and JOSHUA?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#1035FFate, hello.\x01",
            "I'm sorry I haven't been around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Hah! Look at you!\x01",
            "Getting all manly like this in the\x01",
            "few months you've been away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Ah, but that's a relief. Looks like you're\x01",
            "doing good as a bracer alongside Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1040FI've...been trying.\x01",
            "Thank you, Fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Seems like the entire kingdom's gone\x01",
            "completely mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I'm sure old Cassius is busy as all\x01",
            "hell just keeping it all together.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #7
        0xFE,
        (
            "You two work just as hard to help,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006FNo worries on that account.\x01",
            "We'll bust our butts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1040FIf anything comes up, don't hesitate\x01",
            "to visit the guild.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #10
        0xFE,
        (
            "You bet I will.\x01",
            "Take care, you two.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x209B)
    Jump("loc_9E8")

    label("loc_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_84D")

    ChrTalk(    #11
        0xFE,
        (
            "If anything at all comes up,\x01",
            "I'll let Aina and the guild know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "You two take care.\x02",
    )

    CloseMessageWindow()
    OP_A3(0x1)
    Jump("loc_9E8")

    label("loc_84D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_981")

    ChrTalk(    #13
        0xFE,
        (
            "Ah, that's right, there's a wedding\x01",
            "happening over at the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "A wedded couple's start in THIS mess.\x01",
            "Talk about bad luck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I can only imagine the dread the\x01",
            "parents are feeling, what with having\x01",
            "a daughter of my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "*sigh* I hope Yuni's wedding day is a\x01",
            "peaceful one...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_9E8")

    label("loc_981")


    ChrTalk(    #17
        0xFE,
        "A wedding in the middle of all this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "*sigh* I hope Yuni's wedding day is a\x01",
            "peaceful one...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E8")

    Jump("loc_16A5")

    label("loc_9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_B1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A67")

    ChrTalk(    #19
        0xFE,
        "Yuni refuses to leave my side.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Gets me right here...\x01",
            "Guess Yuni does understand how\x01",
            "much I care.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B18")

    label("loc_A67")


    ChrTalk(    #21
        0xFE,
        (
            "I told her she can go outside, but now\x01",
            "Yuni refuses to leave my side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Guess Yuni really does understand\x01",
            "how I feel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "Heh... Nah, there's nothin' in my eye...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B18")

    Jump("loc_16A5")

    label("loc_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BD2")

    ChrTalk(    #24
        0xFE,
        (
            "Even with Ashton and his squad in town,\x01",
            "we can't be careless with the fog still\x01",
            "this thick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Anyway, I want to have Yuni somewhere\x01",
            "I can keep an eye on her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA5")

    label("loc_BD2")


    ChrTalk(    #26
        0xFE,
        (
            "So Ashton's squad will be guarding the\x01",
            "town directly, eh? Good call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "We still can't be careless with the\x01",
            "fog this thick, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Anyway, I want to have Yuni somewhere\x01",
            "I can keep an eye on her.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_CA5")

    Jump("loc_16A5")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_E8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D5A")

    ChrTalk(    #29
        0xFE,
        "Yuni seems to be avoiding me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Even if it was to keep her safe,\x01",
            "it's not like me to yell at her\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "This whole situation is depressing...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E87")

    label("loc_D5A")


    ChrTalk(    #32
        0xFE,
        (
            "This morning I found Yuni breaking the\x01",
            "rules I set and going outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "When I realized what she had done...\x01",
            "I'll admit I lost my cool and raised my\x01",
            "voice to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Even if it's about Yuni's safety,\x01",
            "it's not like me to forget myself like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Yuni may hate me now,\x01",
            "I don't know...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E87")

    Jump("loc_16A5")

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_13C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 0)), scpexpr(EXPR_END)), "loc_1138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F4F")

    ChrTalk(    #36
        0xFE,
        (
            "They should be signing the non-aggression\x01",
            "pact right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Maybe it's a bit optimistic of me,\x01",
            "but I feel like the kingdom's future\x01",
            "is looking bright.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1048")

    label("loc_F4F")


    ChrTalk(    #38
        0xFE,
        (
            "That reminds me, the non-aggression pact\x01",
            "signing should be starting very soon now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I'm sure Cassius is busy keeping that safe,\x01",
            "along with everything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Still, it's a hugely important moment for\x01",
            "the country. I hope it goes well.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1048")

    Jump("loc_1135")

    label("loc_104B")


    ChrTalk(    #41
        0xFE,
        (
            "The Rolent guildhouse seems to really\x01",
            "be hurting for bodies of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "After all, Cassius isn't a bracer anymore,\x01",
            "and Scherazard's been away too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Now that you both are back in town,\x01",
            "you'd better fill in a bit, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1135")

    Jump("loc_13C5")

    label("loc_1138")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #44
        0xFE,
        "Ah, Estelle, Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I haven't seen either of you in ages.\x01",
            "Have you been well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1016FPretty much, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x103,
        "#020FWe've been busy, needless to say.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 4)), scpexpr(EXPR_END)), "loc_1266")

    ChrTalk(    #48
        0xFE,
        "I see. I'm glad you're both well!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Looks like you're both doing good jobs\x01",
            "as bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DB")

    label("loc_1266")


    ChrTalk(    #50
        0xFE,
        (
            "I heard from Aina. You've become a\x01",
            "senior bracer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "That's wonderful!\x01",
            "You're really doing a good job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DB")


    ChrTalk(    #52
        0x101,
        "#1008FAhaha... Well, y'know, doin' what I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "It seems like the Rolent guildhouse has\x01",
            "been hit hard with personnel shortages\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I hope you can give them the hand they\x01",
            "need in your father's absence, Estelle!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1890)
    OP_A2(0x1)

    label("loc_13C5")

    Jump("loc_16A5")

    label("loc_13C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_16A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 4)), scpexpr(EXPR_END)), "loc_149E")

    ChrTalk(    #55
        0xFE,
        (
            "The coup really surprised us all,\x01",
            "but in the end, maybe it'll help the\x01",
            "kingdom come closer together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I'm just glad it seems like we'll be able\x01",
            "to entrust a bright future to our children.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A5")

    label("loc_149E")


    ChrTalk(    #57
        0xFE,
        "Estelle! When did you get back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#000FJust a moment ago, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I heard from Aina.\x01",
            "You've become a full bracer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Sounds like that trip of yours was\x01",
            "worthwhile!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#008FAh, haha... Yeah, pretty...pretty much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "From what I heard, it sounds like Cassius\x01",
            "has rejoined the Royal Army, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "The coup really surprised us all,\x01",
            "but in the end, maybe it'll help the\x01",
            "kingdom come closer together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "I'm just glad it seems like we'll be able\x01",
            "to entrust a bright future to our children.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1034)

    label("loc_16A5")

    TalkEnd(0xB)
    Return()

    # Function_4_4FE end

    def Function_5_16A9(): pass

    label("Function_5_16A9")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_171A")

    ChrTalk(    #65
        0xFE,
        "Awww. Papa's worrying about stuff again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "I don't really get why.\x01",
            "Is it because I'm seven?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8B")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_182A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C3")

    ChrTalk(    #67
        0xFE,
        (
            "Papa's away, so I'm taking care\x01",
            "of the house!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "But, but the lights won't turn on in\x01",
            "my room, so it's scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "Papa, come home soon...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1827")

    label("loc_17C3")


    ChrTalk(    #70
        0xFE,
        (
            "The lights in my room won't turn on,\x01",
            "so it's scary being alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "Papa, come home soon...\x02",
    )

    CloseMessageWindow()

    label("loc_1827")

    Jump("loc_1C8B")

    label("loc_182A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_188E")

    ChrTalk(    #72
        0xFE,
        (
            "Heehee! Today I get ta spend aaaaaall\x01",
            "day with Papa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "I'm happy! I love my papa!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C8B")

    label("loc_188E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_19EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18F1")

    ChrTalk(    #74
        0xFE,
        "I have to say sorry to Papa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I called him a meanie!\x01",
            "And that's wrong!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E7")

    label("loc_18F1")


    ChrTalk(    #76
        0xFE,
        (
            "Is it true the soldiers outside are\x01",
            "protectin' us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "I didn't know it was dangerous outside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "*gasp* That's why Papa didn't want me\x01",
            "to go outside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "I have to say sorry to Papa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I called him a meanie!\x01",
            "And that's wrong!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_19E7")

    Jump("loc_1C8B")

    label("loc_19EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A13")

    ChrTalk(    #81
        0xFE,
        "Papa's a meanie...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A54")

    label("loc_1A13")


    ChrTalk(    #82
        0xFE,
        "Papa's a meanie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "I'm not gonna talk to him again!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1A54")

    Jump("loc_1C8B")

    label("loc_1A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AB4")

    ChrTalk(    #84
        0xFE,
        "Papa told me not to go outside at all today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "...Papa, you meanie!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B6E")

    label("loc_1AB4")


    ChrTalk(    #86
        0xFE,
        "Ah, Estelle, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "Listen, listen! Papa's such a meanie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "He said I can't go outside today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I told him it's just a little fog,\x01",
            "but he won't listen at aaaaaall!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1B6E")

    Jump("loc_1C8B")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_1C8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1BD0")

    ChrTalk(    #90
        0xFE,
        "Estelle, have you seen Luke yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "He's been talkin' about you a lot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C8B")

    label("loc_1BD0")


    ChrTalk(    #92
        0xFE,
        "Ahhh! Esteeelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#001FHey, Yuni! You been okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "Uh-huh! I'm okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "Estelle, have you seen Luke yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "He's been talkin' about you a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#505FHe has? Huh...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1C8B")

    TalkEnd(0xC)
    Return()

    # Function_5_16A9 end

    def Function_6_1C8F(): pass

    label("Function_6_1C8F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_1E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9F")

    ChrTalk(    #98
        0xFE,
        "Hmm... That's odd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "The wedding should be over, but Euri\x01",
            "and Freemont aren't back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "I wonder what they're up to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Ho ho ho ho!\x01",
            "Ah, well, that's fine, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "After all, the closer they get,\x01",
            "the sooner I'll see my grandchild!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1E52")

    label("loc_1D9F")


    ChrTalk(    #103
        0xFE,
        (
            "Seems like my Euri and Freemont are\x01",
            "off somewhere besides the wedding...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Well, that's all right, too.\x01",
            "The closer they get, the sooner I'll\x01",
            "meet my grandchild! Ho ho ho!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E52")

    Jump("loc_22F2")

    label("loc_1E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1FAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1F")

    ChrTalk(    #105
        0xFE,
        "Ah, bracer folk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "My daughter and her husband are\x01",
            "off at the wedding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "One young married couple helping\x01",
            "another get started...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Ho ho ho!\x01",
            "Warms the heart, it does.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1FAB")

    label("loc_1F1F")


    ChrTalk(    #109
        0xFE,
        (
            "My daughter and her husband are\x01",
            "off at the wedding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Ah, it's a shame the times are what they\x01",
            "are for such an event, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAB")

    Jump("loc_22F2")

    label("loc_1FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_211E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FDD")

    ChrTalk(    #111
        0xFE,
        "Ah, bracer folk.\x02",
    )

    CloseMessageWindow()

    label("loc_1FDD")


    ChrTalk(    #112
        0xFE,
        (
            "For some reason, the orbal devices\x01",
            "in the house aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Could they all have broke at once?\x01",
            "Hmph. In my day, things were built\x01",
            "to last!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_211B")

    label("loc_207C")


    ChrTalk(    #114
        0xFE,
        (
            "The orbal devices in the house\x01",
            "aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I'll have to send Freemont down to\x01",
            "Melders' place later and let that old\x01",
            "busybody sort it out. Ho ho!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211B")

    Jump("loc_22F2")

    label("loc_211E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_22F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_21D1")

    ChrTalk(    #116
        0xFE,
        (
            "My son-in-law works hard enough,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "He's the only one who can take up the\x01",
            "family business and uphold the old\x01",
            "tradition of Rolent wood crafting!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F2")

    label("loc_21D1")


    ChrTalk(    #118
        0xFE,
        (
            "There's a great Servais tree in the\x01",
            "heart of Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "It's said there was once a spirit who\x01",
            "dwelled in it and loved pranks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Supposedly, it showed people illusions\x01",
            "or confused their path with fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "But, it's just a fairy tale.\x01",
            "No one's seen the like of that in ages.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_22F2")

    TalkEnd(0x8)
    Return()

    # Function_6_1C8F end

    def Function_7_22F6(): pass

    label("Function_7_22F6")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2457")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2382")

    ChrTalk(    #122
        0xFE,
        (
            "I'm glad this happened when there\x01",
            "wasn't any work to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "It means I can focus on taking\x01",
            "care of Radford.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2454")

    label("loc_2382")


    ChrTalk(    #124
        0xFE,
        (
            "I actually just finished with the\x01",
            "seedling planting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "We can't ship any lumber like this,\x01",
            "so for now I have no work to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "In a way, it's good timing.\x01",
            "It gives me time to take care of Radford.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2454")

    Jump("loc_25AD")

    label("loc_2457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_25AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_24E8")

    ChrTalk(    #127
        0xFE,
        (
            "Radford sure has a happy expression\x01",
            "on his face for a man out like a light!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "I wonder what kind of dreams he's having.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25AD")

    label("loc_24E8")


    ChrTalk(    #129
        0xFE,
        "Hey, came today, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "Radford's still out like a light,\x01",
            "I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "The one silver lining is that he seems to\x01",
            "be having some real nice dreams, given\x01",
            "the expression on his face...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_25AD")

    TalkEnd(0xA)
    Return()

    # Function_7_22F6 end

    def Function_8_25B1(): pass

    label("Function_8_25B1")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 4)), scpexpr(EXPR_END)), "loc_274D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B8")

    ChrTalk(    #132
        0xFE,
        (
            "The second Father woke up, he sent\x01",
            "Freemont packing off to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "All night taking care of Father, and\x01",
            "then right back to work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Even though they've gotten friendlier,\x01",
            "Father is still a stickler for the\x01",
            "family business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_274A")

    label("loc_26B8")


    ChrTalk(    #135
        0xFE,
        (
            "We really do owe you everything for\x01",
            "what you've done this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "I'll keep a close eye on Father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "Everyone, be careful on your way!\x02",
    )

    CloseMessageWindow()

    label("loc_274A")

    Jump("loc_2A2A")

    label("loc_274D")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #138
        0xFE,
        "Oh, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "My father woke up and is perfectly\x01",
            "healthy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "Really, I... Thank you, whatever you did!\x01",
            "I don't know how I can truly thank you,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#1025FEr, nooo, you don't need to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x103,
        (
            "#020FHow IS Radford doing, anyway?\x01",
            "You said he's well?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #143
        0xFE,
        "Very much so, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "He's still a little light-headed,\x01",
            "but I think that will pass soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1011FGood. Sounds like he's fine, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x103,
        (
            "#026FYes, I suspect he'll be fine.\x02\x03",

            "#020FIf there's any change, let Father Divine\x01",
            "know.\x02\x03",

            "He should be able to help at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "Yes, I will. I'm keeping a very close\x01",
            "eye on Father's health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "Anyway, please be careful on your way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#1006FWe will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x103,
        "#020FWe'll be seeing you, Euridice.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A5C)
    OP_A2(0x5)

    label("loc_2A2A")

    Jump("loc_2FAD")

    label("loc_2A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2C64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2B26")

    ChrTalk(    #151
        0xFE,
        (
            "I appreciate that Freemont's worried\x01",
            "about my father, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "At the rate he's going, he's going to\x01",
            "end up in a full-blown coma before\x01",
            "Father does!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "Oh, Aidios, I'm going to MAKE him\x01",
            "let me take over for a while today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C61")

    label("loc_2B26")


    ChrTalk(    #154
        0xFE,
        (
            "Freemont, my husband, has been taking\x01",
            "care of Father without getting a wink of\x01",
            "sleep himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "I told him I could take over,\x01",
            "but he just won't go to bed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "Oooh, at this rate, HE'LL end up in a\x01",
            "proper coma before Father does!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Aidios' Mercy, I'm going to MAKE him\x01",
            "let me take over for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2C61")

    Jump("loc_2FAD")

    label("loc_2C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2CD9")

    ChrTalk(    #158
        0xFE,
        (
            "The fog seems like it's even deeper\x01",
            "than it was yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "I hope nothing more happens...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D88")

    label("loc_2CD9")


    ChrTalk(    #160
        0xFE,
        (
            "The fog seems like it's even deeper\x01",
            "than it was yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "Father is still asleep, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "I hope nothing more happens...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "Dear Aidios...please deliver us!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2D88")

    Jump("loc_2FAD")

    label("loc_2D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2E22")

    ChrTalk(    #164
        0xFE,
        (
            "My father's finally accepted my husband\x01",
            "as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Things are going so well, I'm\x01",
            "almost scared for the other shoe to drop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F19")

    label("loc_2E22")


    ChrTalk(    #166
        0xFE,
        (
            "Freemont, my husband, had been killing\x01",
            "himself at work trying to please my father\x01",
            "until recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "But now it seems like he's been able to\x01",
            "relax his pace and work more comfortably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "He's also getting along much better\x01",
            "with Father.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2F19")

    Jump("loc_2FAD")

    label("loc_2F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_2FAD")

    ChrTalk(    #169
        0xFE,
        "Freemont's work is going very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "And he's getting along much better\x01",
            "with my father, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "I'm just...so happy right now.\x02",
    )

    CloseMessageWindow()

    label("loc_2FAD")

    TalkEnd(0x9)
    Return()

    # Function_8_25B1 end

    def Function_9_2FB1(): pass

    label("Function_9_2FB1")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_31C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_3121")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3031")

    ChrTalk(    #172
        0xF,
        (
            "I'm counting on you with that letter,\x01",
            "Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xF,
        "Once you find it, come back immediately.\x02",
    )

    CloseMessageWindow()
    Jump("loc_311E")

    label("loc_3031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_30B9")

    ChrTalk(    #174
        0xF,
        (
            "I'm counting on you, Estelle.\x01",
            "Find that commission letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xF,
        (
            "Without it, I'm too worried to even\x01",
            "begin working again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_311E")

    label("loc_30B9")


    ChrTalk(    #176
        0xF,
        "Hey, Estelle. How's the search going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xF,
        (
            "I'm counting on you.\x01",
            "Find that commission letter!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_311E")

    Jump("loc_31C6")

    label("loc_3121")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3144")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_313D")
    Call(1, 1)
    Jump("loc_3141")

    label("loc_313D")

    Call(1, 0)

    label("loc_3141")

    Jump("loc_31C6")

    label("loc_3144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_316B")

    ChrTalk(    #178
        0xF,
        "Hrrmmmmmm. This is bad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31C6")

    label("loc_316B")


    ChrTalk(    #179
        0xF,
        "Hrrmmmmmm. This is bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xF,
        (
            "It just HAD to go missing as we started\x01",
            "work again...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_31C6")

    Jump("loc_364F")

    label("loc_31C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_340F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_326C")

    ChrTalk(    #181
        0xF,
        (
            "That...fog creature that attacked us\x01",
            "on the road was a hell of a thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xF,
        (
            "That one bracer tried cutting it in half,\x01",
            "but it just vanished!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_340C")

    label("loc_326C")


    ChrTalk(    #183
        0xF,
        (
            "Damn... To think the fog'd climb that\x01",
            "far up the mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xF,
        (
            "We couldn't keep working like that,\x01",
            "so we were just killing time when we\x01",
            "got word from the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xF,
        (
            "They sent a few bracers, so we managed\x01",
            "to get back to town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xF,
        (
            "We did get attacked by some...some\x01",
            "damned fog monsters on the way\x01",
            "back down the mountain road, though!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xF,
        (
            "If the bracers hadn't been there,\x01",
            "we would've been in real trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_340C")

    Jump("loc_364F")

    label("loc_340F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_364F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 2)), scpexpr(EXPR_END)), "loc_34AC")

    ChrTalk(    #188
        0xF,
        "Today's a day to spend with family.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xF,
        (
            "Feels like the right thing to do\x01",
            "since I've been stuffed up in that\x01",
            "mine all the time lately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_364F")

    label("loc_34AC")


    ChrTalk(    #190
        0xF,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xF,
        (
            "Say, you're Cassius' girl, the bracer\x01",
            "who helped us before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#501FYes! Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xF,
        (
            "Thanks to you, our mining of a\x01",
            "new vein's going just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xF,
        (
            "After what happened, we closed up that\x01",
            "hole the monsters came out of with some\x01",
            "explosives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#506FUm, well, glad to hear it ended well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xF,
        "Wasn't really any other way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xF,
        (
            "It was worth it, though.\x01",
            "Ol' Malga's running just fine now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1032)

    label("loc_364F")

    TalkEnd(0xF)
    Return()

    # Function_9_2FB1 end

    def Function_10_3653(): pass

    label("Function_10_3653")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_386B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C2")

    ChrTalk(    #198
        0xFE,
        (
            "A little while ago, my husband just\x01",
            "came back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Apparently there was a little trouble\x01",
            "at the mine, but it seems they're going\x01",
            "to keep working anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "You'd think if he was coming home, he'd\x01",
            "at least STAY home at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "Well, I know that stubborn head of his,\x01",
            "and there's no stopping him when he's\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3868")

    label("loc_37C2")


    ChrTalk(    #202
        0xFE,
        (
            "My husband returned from the mine\x01",
            "a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "Apparently there was a little trouble\x01",
            "at the mine, but it seems they're going\x01",
            "to keep working anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3868")

    Jump("loc_41E4")

    label("loc_386B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_39C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393B")

    ChrTalk(    #204
        0xFE,
        (
            "I can't help but be worried with the\x01",
            "orbments all out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "They've just started some construction\x01",
            "work at the mine, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "I hope there aren't any accidents or\x01",
            "problems...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_39C0")

    label("loc_393B")


    ChrTalk(    #207
        0xFE,
        (
            "I can't help but be worried with the\x01",
            "orbments all out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "They've just started some construction\x01",
            "work at the mine, you see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C0")

    Jump("loc_41E4")

    label("loc_39C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3CFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3A50")

    ChrTalk(    #209
        0xFE,
        (
            "I know the reason he works so hard\x01",
            "is for us, his family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "I'll do everything I can to help him\x01",
            "in turn!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B81")

    label("loc_3A50")


    ChrTalk(    #211
        0xFE,
        (
            "Returning to work the second the fog\x01",
            "clears...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "I guess things are really that busy\x01",
            "over at the Malga Mine right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "I do wish he'd rest a bit after the\x01",
            "incident with the fog...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "But I know the reason he works so\x01",
            "hard is for us, his family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "I can't really complain, given that.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3B81")

    Jump("loc_3CF7")

    label("loc_3B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3BE9")

    ChrTalk(    #216
        0xFE,
        "I understand you helped my husband.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "Thank you for everything you've done\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CF7")

    label("loc_3BE9")


    ChrTalk(    #218
        0xFE,
        (
            "My husband's supposed to start work\x01",
            "again at the mine today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "Apparently he lost something very\x01",
            "important and hasn't headed out yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "I hope the other miners can manage things\x01",
            "for a while... Knowing a few of them, though,\x01",
            "it's a bit of a question...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CF7")

    Jump("loc_41E4")

    label("loc_3CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3D5E")

    ChrTalk(    #221
        0xFE,
        (
            "Well, I'm just glad my husband's home\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "All thanks to you bracers!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E31")

    label("loc_3D5E")


    ChrTalk(    #223
        0xFE,
        (
            "Ahh, thank Aidios.\x01",
            "My husband's back safe from the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "Apparently some bracers escorted\x01",
            "him back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "To think this fog goes all the way up the\x01",
            "mountain... Just what's going on here?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3E31")

    Jump("loc_41E4")

    label("loc_3E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3F3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3E9B")

    ChrTalk(    #226
        0xFE,
        (
            "Was my husband able to get to\x01",
            "the mine safely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "I hope he didn't get lost...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F3A")

    label("loc_3E9B")


    ChrTalk(    #228
        0xFE,
        (
            "Look at the fog!\x01",
            "It's terrible today, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "I'm worried about my husband.\x01",
            "Was he able to get to the mine safely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        "I hope he didn't get lost...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3F3A")

    Jump("loc_41E4")

    label("loc_3F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_419C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4049")

    ChrTalk(    #231
        0xFE,
        (
            "Maybe it's because she sees him so\x01",
            "little, but my Anya adores her father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "I'm glad we're a happy family, ultimately,\x01",
            "even if Gaton has to be absent so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "Fifteen years since I married him,\x01",
            "and I still don't feel tired of it at all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4199")

    label("loc_4049")


    ChrTalk(    #234
        0xFE,
        (
            "My husband's been at the mine for four\x01",
            "days now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "This is about when my Anya starts to get\x01",
            "a little hard to handle, since she wants\x01",
            "to see her daddy so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "Maybe it's because she sees him\x01",
            "so little, but she adores her father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "I'm glad we're a happy family, ultimately,\x01",
            "even if Gaton has to be absent so often.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4199")

    Jump("loc_41E4")

    label("loc_419C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_41E4")

    ChrTalk(    #238
        0xFE,
        (
            "Since Gaton is home today, I'm going\x01",
            "all-out on this lunch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E4")

    TalkEnd(0xD)
    Return()

    # Function_10_3653 end

    def Function_11_41E8(): pass

    label("Function_11_41E8")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_424F")

    ChrTalk(    #239
        0xFE,
        "Daddy came home a little while ago!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        "But then he had to go right back to work...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4733")

    label("loc_424F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_42A3")

    ChrTalk(    #241
        0xFE,
        "I think Mommy's thinking about stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "Did something bad happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4733")

    label("loc_42A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_4360")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4324")

    ChrTalk(    #243
        0xFE,
        "Awww. Daddy went to work again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        "I wonder how long he'll be gone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "I hope he comes home soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_435D")

    label("loc_4324")


    ChrTalk(    #246
        0xFE,
        "Daddy looks worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "I wonder what happened...\x02",
    )

    CloseMessageWindow()

    label("loc_435D")

    Jump("loc_4733")

    label("loc_4360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_4497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_43D0")

    ChrTalk(    #248
        0xFE,
        (
            "A nice man with red hair brought\x01",
            "Daddy home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "Heeheehee!\x01",
            "I'm so glad Daddy's home! ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4494")

    label("loc_43D0")


    ChrTalk(    #250
        0xFE,
        (
            "A nice man with red hair brought\x01",
            "Daddy home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "The man said that the fog's gotten to\x01",
            "the mine, too, so everybody had to\x01",
            "ee-back-you-ate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "Heeheeheeeee!\x01",
            "I'm so glad Daddy's home! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_4494")

    Jump("loc_4733")

    label("loc_4497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_458C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4510")

    ChrTalk(    #253
        0xFE,
        "Daddy always leaves the house so early.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "I try to get up early, but I never see\x01",
            "Daddy leave...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4589")

    label("loc_4510")


    ChrTalk(    #255
        0xFE,
        "Daddy always leaves the house so early.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "I try to get up early, but I never see\x01",
            "Daddy leave...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "Awwww...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_4589")

    Jump("loc_4733")

    label("loc_458C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_46C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4611")

    ChrTalk(    #258
        0xFE,
        "Aww, I haven't seen Daddy in foreeeever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "I wanna see Daddy soooon!\x01",
            "And then I wanna go on another picnic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46C4")

    label("loc_4611")


    ChrTalk(    #260
        0xFE,
        "Daddy's really busy with work right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "Aww, I haven't seen Daddy in foreeeever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "The picnic was so fun, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "I wanna go back to the farm\x01",
            "with Daddy again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_46C4")

    Jump("loc_4733")

    label("loc_46C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_4733")

    ChrTalk(    #264
        0xFE,
        "Heehee! Daddy's taking a day off today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "And we're gonna go on a picnic\x01",
            "to the Perzel farm!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4733")

    TalkEnd(0xE)
    Return()

    # Function_11_41E8 end

    def Function_12_4737(): pass

    label("Function_12_4737")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x8, -42510, 0, 37680, 238)
    SetChrPos(0x9, -43770, 0, 36860, 59)
    SetChrPos(0xA, -43000, 0, 36530, 10)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_6F(0x2, 0)
    OP_6D(-39410, 0, 35550, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)

    def lambda_47F4():
        OP_6D(-43060, 0, 37080, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_47F4)
    Sleep(1500)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_95(0x8, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 90, 400)
    OP_8C(0x8, 0, 400)
    OP_8C(0x8, 270, 400)
    OP_8C(0x8, 238, 400)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0410   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_12_4737 end

    SaveToFile()

Try(main)
