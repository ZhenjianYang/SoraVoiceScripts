from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4220   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4220.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Captain Amalthea',                     # 9
        '2nd Lieutenant Lorence',               # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Cassius',                              # 15
        'General Morgan',                       # 16
        'Queen Alicia',                         # 17
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH02100 ._CH',             # 03
        'ED6_DT07/CH02200 ._CH',             # 04
        'ED6_DT07/CH01330 ._CH',             # 05
        'ED6_DT07/CH02000 ._CH',             # 06
        'ED6_DT07/CH02080 ._CH',             # 07
        'ED6_DT07/CH02013 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH02100P._CP',             # 03
        'ED6_DT07/CH02200P._CP',             # 04
        'ED6_DT07/CH01330P._CP',             # 05
        'ED6_DT07/CH02000P._CP',             # 06
        'ED6_DT07/CH02080P._CP',             # 07
        'ED6_DT07/CH02013P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 40,
        Z                   = 750,
        Y                   = 155220,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_2B5",          # 01, 1
        "Function_2_2BF",          # 02, 2
        "Function_3_43C",          # 03, 3
        "Function_4_5C3",          # 04, 4
        "Function_5_71E",          # 05, 5
        "Function_6_A26",          # 06, 6
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_220")
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_254")
    Jump("loc_2B4")

    label("loc_254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_28F")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xE, 530, 0, 150340, 0)
    SetChrPos(0xF, -400, 0, 150340, 0)
    Jump("loc_2B4")

    label("loc_28F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_299")
    Jump("loc_2B4")

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_2A3")
    Jump("loc_2B4")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_2AD")
    Jump("loc_2B4")

    label("loc_2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2B4")

    label("loc_2B4")

    Return()

    # Function_0_212 end

    def Function_1_2B5(): pass

    label("Function_1_2B5")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_2B5 end

    def Function_2_2BF(): pass

    label("Function_2_2BF")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_426")

    label("loc_2E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_426")

    label("loc_2FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_426")

    label("loc_316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_426")

    label("loc_32F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_426")

    label("loc_348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_426")

    label("loc_361")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_426")

    label("loc_37A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_393")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_426")

    label("loc_393")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_426")

    label("loc_3AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_426")

    label("loc_3C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_426")

    label("loc_3DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_426")

    label("loc_3F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_410")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_426")

    label("loc_410")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_426")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_426")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_426")

    label("loc_43B")

    Return()

    # Function_2_2BF end

    def Function_3_43C(): pass

    label("Function_3_43C")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_461")
    SetChrSubChip(0xFE, 1)
    Jump("loc_47C")

    label("loc_461")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_477")
    SetChrSubChip(0xFE, 0)
    Jump("loc_47C")

    label("loc_477")

    SetChrSubChip(0xFE, 2)

    label("loc_47C")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #0
        0x10,
        (
            "#090FIt pains me to request that you return\x01",
            "to service after closing that chapter\x01",
            "of your life, Cassius...\x02\x03",

            "But, gentle though you be, I know\x01",
            "you have an iron will. And I know\x01",
            "you will do what you must.\x02\x03",

            "My sincerest apologies to you, but\x01",
            "I ask if you could lend me your\x01",
            "father's strength for a time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_43C end

    def Function_4_5C3(): pass

    label("Function_4_5C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_652")

    ChrTalk(    #1
        0xE,
        (
            "#080FI have some important matters\x01",
            "to discuss at the moment.\x02\x03",

            "You two go and enjoy the festivities\x01",
            "without me, if you would.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A")

    label("loc_652")

    OP_A2(0x0)

    ChrTalk(    #2
        0xE,
        (
            "#080FThe town square must be alight\x01",
            "with activity right about now.\x02\x03",

            "But I have some important matters\x01",
            "to discuss at the moment.\x02\x03",

            "You two go and enjoy the festivities\x01",
            "without me, if you would.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71A")

    TalkEnd(0xFE)
    Return()

    # Function_4_5C3 end

    def Function_5_71E(): pass

    label("Function_5_71E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_74E")

    ChrTalk(    #3
        0xF,
        "#163FRichard... That idiot...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A22")

    label("loc_74E")

    OP_A2(0x1)

    ChrTalk(    #4
        0xF,
        "#161FWell, hello. It's been a while!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#004FGeneral Morgan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#010FIt has been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xF,
        (
            "#163FI heard you saved my granddaughter\x01",
            "out at the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#505FThe Villa...\x02\x03",

            "#001FOh, yeah! Rianne!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#010FWe only did what was needed.\x02\x03",

            "It's the life of a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xF,
        (
            "#160FOh, stop with the humbleness\x01",
            "already. You're much too young\x01",
            "for that!\x02\x03",

            "In the end, you saved not just\x01",
            "the Villa, but Her Majesty and,\x01",
            "indeed, the kingdom itself!\x02\x03",

            "This time, I'm going to thank\x01",
            "you properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#002FGeneral...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xF,
        "#160FYou two...did well. Very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#505F...I've got to say, I've heard\x01",
            "much more heartfelt thank yous\x01",
            "in my time.\x02\x03",

            "#000FBut not from you, General. So...\x01",
            "uh...thanks for the thanks!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A22")

    TalkEnd(0xFE)
    Return()

    # Function_5_71E end

    def Function_6_A26(): pass

    label("Function_6_A26")

    EventBegin(0x0)
    OP_6D(-400, 500, 150910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 380, 500, 150540, 270)
    SetChrPos(0x9, -1300, 500, 151320, 138)
    SetChrPos(0xA, -1070, 0, 147120, 0)
    SetChrPos(0xB, 750, 0, 147120, 0)
    SetChrPos(0xC, -1190, 0, 145180, 0)
    SetChrPos(0xD, 820, 0, 145210, 0)

    ChrTalk(    #14
        0x8,
        (
            "#180FWha...\x01",
            "What's the meaning of this?!\x02\x03",

            "How can we have lost contact\x01",
            "with the Erbe Royal Villa?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#280FThe Royal Guardsmen\x01",
            "or the bracers...\x02\x03",

            "This has to mean that one\x01",
            "or the other shut it down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#180FThose interfering little...\x02\x03",

            "Were you not in command of that\x01",
            "division, 2nd Lieutenant?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "#280FIt is a pity...\x02\x03",

            "But what's done is done. Obsessing\x01",
            "about it now will accomplish nothing.\x02\x03",

            "Furthermore, we must strengthen\x01",
            "the castle's defenses to ensure\x01",
            "that Her Majesty is not taken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "#180FI don't need you to tell me that!\x02",
    )

    CloseMessageWindow()

    def lambda_D0F():
        OP_6D(520, 0, 148610, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D0F)
    OP_8C(0x8, 180, 400)
    Sleep(1000)

    ChrTalk(    #19
        0x8,
        (
            "#180FI want the castle gate sealed!\x01",
            "Not a soul is to enter from\x01",
            "here on out!\x02\x03",

            "The only attacks I should need\x01",
            "to worry about are the ones\x01",
            "that come from the sky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xA,
        "Yes, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#180FOnce that's done, scrape up troops from\x01",
            "wherever you can find them--anywhere in\x01",
            "Liberl--and send them to the villa!\x02\x03",

            "Priority one is to subjugate the\x01",
            "terrorists who deceived the royal\x01",
            "family!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        "Yes, ma'am!\x02",
    )

    CloseMessageWindow()

    def lambda_EC5():
        OP_8E(0xFE, 0xBE, 0x0, 0x1AE8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_EC5)

    def lambda_EE0():
        OP_8E(0xFE, 0xBE, 0x0, 0x1AE8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EE0)
    Sleep(300)

    def lambda_F00():
        OP_8E(0xFE, 0xBE, 0x0, 0x1AE8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F00)

    def lambda_F1B():
        OP_8E(0xFE, 0xBE, 0x0, 0x1AE8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F1B)
    Sleep(1000)
    OP_6D(-400, 500, 150910, 1000)

    ChrTalk(    #23
        0x9,
        "#280FHa ha... Nicely done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#180FHmph... Of course it was. I've\x01",
            "served with this unit for some\x01",
            "time, unlike you.\x02\x03",

            "I swear, I WILL protect this castle while His\x01",
            "Excellency is absent...no matter the cost!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4300   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_A26 end

    SaveToFile()

Try(main)
