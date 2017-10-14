from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5503   ._SN',
        MapName             = 'Other',
        Location            = 'C5503.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        'Kurt',                                 # 9
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Monster',                              # 13
        'Target Camera',                        # 14
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
        'ED6_DT07/CH01620 ._CH',             # 00
        'ED6_DT29/CH12220 ._CH',             # 01
        'ED6_DT07/CH00410 ._CH',             # 02
        'ED6_DT07/CH00414 ._CH',             # 03
        'ED6_DT07/CH00411 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00420 ._CH',             # 06
        'ED6_DT29/CH12210 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01620P._CP',             # 00
        'ED6_DT29/CH12220P._CP',             # 01
        'ED6_DT07/CH00410P._CP',             # 02
        'ED6_DT07/CH00414P._CP',             # 03
        'ED6_DT07/CH00411P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00420P._CP',             # 06
        'ED6_DT29/CH12210P._CP',             # 07
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -13940,
        Z                   = 0,
        Y                   = 19260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -27580,
        Z                   = 0,
        Y                   = 27680,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -36160,
        Z                   = 0,
        Y                   = 35380,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -36190,
        Z                   = 0,
        Y                   = 46820,
        Direction           = 170,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0xC0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 7400,
        Y                   = 2500,
        Z                   = 3900,
        Range               = 9700,
        Unknown_10          = 0x1A90,
        Unknown_14          = 0x2008,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -7750,
        Y                   = 0,
        Z                   = 199430,
        Range               = -4280,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x31ECA,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -16720,
        Y                   = -1000,
        Z                   = 19250,
        Range               = -11910,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x3B92,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -24000,
        Y                   = -1000,
        Z                   = 30610,
        Range               = -25500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x634C,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -38590,
        Y                   = -1000,
        Z                   = 33670,
        Range               = -33820,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7B0C,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -38410,
        Y                   = -1000,
        Z                   = 46310,
        Range               = -33920,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xA21C,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    DeclActor(
        TriggerX            = 31770,
        TriggerZ            = 200,
        TriggerY            = 202040,
        TriggerRange        = 800,
        ActorX              = 31770,
        ActorZ              = 1200,
        ActorY              = 202040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5000,
        TriggerZ            = 0,
        TriggerY            = 6610,
        TriggerRange        = 1600,
        ActorX              = -5000,
        ActorZ              = 1000,
        ActorY              = 6730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_2EF",          # 01, 1
        "Function_2_555",          # 02, 2
        "Function_3_5FC",          # 03, 3
        "Function_4_6AC",          # 04, 4
        "Function_5_1231",         # 05, 5
        "Function_6_1254",         # 06, 6
        "Function_7_174C",         # 07, 7
        "Function_8_21FE",         # 08, 8
        "Function_9_2227",         # 09, 9
        "Function_10_2276",        # 0A, 10
        "Function_11_271D",        # 0B, 11
        "Function_12_29C9",        # 0C, 12
        "Function_13_30FE",        # 0D, 13
        "Function_14_3166",        # 0E, 14
        "Function_15_353A",        # 0F, 15
        "Function_16_35A2",        # 10, 16
        "Function_17_3858",        # 11, 17
        "Function_18_3BDF",        # 12, 18
        "Function_19_3EF7",        # 13, 19
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_2DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE")
    SetChrPos(0x8, -770, 0, 7450, 170)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EE")
    Event(0, 4)

    label("loc_2EE")

    Return()

    # Function_0_2B2 end

    def Function_1_2EF(): pass

    label("Function_1_2EF")

    OP_22(0x1C7, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 0)), scpexpr(EXPR_END)), "loc_300")
    SetChrFlags(0x9, 0x80)

    label("loc_300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 1)), scpexpr(EXPR_END)), "loc_30C")
    SetChrFlags(0xA, 0x80)

    label("loc_30C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 2)), scpexpr(EXPR_END)), "loc_318")
    SetChrFlags(0xB, 0x80)

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 3)), scpexpr(EXPR_END)), "loc_324")
    SetChrFlags(0xC, 0x80)

    label("loc_324")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_378")
    OP_A2(0x1160)
    SetChrFlags(0x9, 0x80)
    Call(0, 8)
    SetChrPos(0x101, -13420, 0, 18940, 0)
    SetChrPos(0x10A, -14920, 0, 18970, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jump("loc_3A7")

    label("loc_378")

    Call(0, 8)
    SetChrPos(0x0, -13990, 50, 12500, 0)
    SetChrPos(0x1, -13990, 50, 12500, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)

    label("loc_3A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F8")
    EventBegin(0x2)
    Call(0, 8)
    SetChrPos(0x0, -23500, 0, 28000, 270)
    SetChrPos(0x1, -23500, 0, 28000, 270)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F8")
    OP_A2(0x1161)
    SetChrFlags(0xA, 0x80)

    label("loc_3F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449")
    EventBegin(0x2)
    Call(0, 8)
    SetChrPos(0x0, -36130, 0, 28500, 0)
    SetChrPos(0x1, -36130, 0, 28500, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_449")
    OP_A2(0x1162)
    SetChrFlags(0xB, 0x80)

    label("loc_449")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CC")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49D")
    OP_A2(0x1163)
    SetChrFlags(0xC, 0x80)
    Call(0, 8)
    SetChrPos(0x0, -36010, 0, 40500, 0)
    SetChrPos(0x1, -36010, 0, 40500, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jump("loc_4CC")

    label("loc_49D")

    Call(0, 8)
    SetChrPos(0x0, -36010, 0, 40500, 0)
    SetChrPos(0x1, -36010, 0, 40500, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_4D6")
    OP_10(0x0, 0x0)

    label("loc_4D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_541")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -5000, 1000, 6730, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x0)
    Jump("loc_554")

    label("loc_541")

    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x0)

    label("loc_554")

    Return()

    # Function_1_2EF end

    def Function_2_555(): pass

    label("Function_2_555")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_586"),
        (1, "loc_592"),
        (2, "loc_59E"),
        (3, "loc_5AA"),
        (4, "loc_5B6"),
        (5, "loc_5C2"),
        (6, "loc_5CE"),
        (SWITCH_DEFAULT, "loc_5DA"),
    )


    label("loc_586")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_5E6")

    label("loc_592")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_5E6")

    label("loc_59E")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_5E6")

    label("loc_5AA")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_5E6")

    label("loc_5B6")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5E6")

    label("loc_5C2")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_5E6")

    label("loc_5CE")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5E6")

    label("loc_5DA")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5E6")

    label("loc_5E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5E6")

    label("loc_5FB")

    Return()

    # Function_2_555 end

    def Function_3_5FC(): pass

    label("Function_3_5FC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_688")

    ChrTalk(    #0
        0x8,
        (
            "#840FIs something wrong, you two?\x02\x03",

            "If you need a moment to rest,\x01",
            "you can use the orbment charging\x01",
            "station over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_6A8")

    label("loc_688")


    ChrTalk(    #1
        0x8,
        "#840FNow, then. Good luck.\x02",
    )

    CloseMessageWindow()

    label("loc_6A8")

    TalkEnd(0x8)
    Return()

    # Function_3_5FC end

    def Function_4_6AC(): pass

    label("Function_4_6AC")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    OP_6D(-13420, 0, 6250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_6FB():
        OP_6D(150, 0, 5990, 5000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_6FB)
    OP_C8(0x200, 0x46, "C_PLAC02._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    Sleep(300)
    SetChrPos(0x8, 7310, 3250, 6000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)

    def lambda_751():
        OP_8E(0x8, 0xFFFFFCE0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_751)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrPos(0xD, 7310, 3250, 6000, 270)
    Sleep(500)

    def lambda_78C():
        OP_8E(0xD, 0x8C, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_78C)

    def lambda_7A7():

        label("loc_7A7")

        OP_69(0xD, 0x0)
        OP_48()
        Jump("loc_7A7")

    QueueWorkItem2(0xD, 3, lambda_7A7)
    Sleep(1000)
    SetChrPos(0x101, 7230, 3000, 5320, 270)
    SetChrPos(0x10A, 7230, 3250, 6550, 270)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10A, 0x80)

    def lambda_7E9():
        OP_8E(0x10A, 0x438, 0x0, 0x1996, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7E9)
    Sleep(500)

    def lambda_809():
        OP_8E(0x101, 0x44C, 0x0, 0x14C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_809)
    WaitChrThread(0x8, 0x1)
    OP_44(0xD, 0x3)
    OP_8C(0x8, 90, 1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #2
        0x101,
        "#4P#1002FSo this is the Balstar Channel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10A,
        (
            "#6P#812FMan, these sewers are HUGE.\x01",
            "What do they keep down here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#6P#843FWell, they're technically smaller\x01",
            "than the sewers beneath Grancel,\x01",
            "but they're still quite sizable.\x02\x03",

            "#840FAs for what is kept down here...\x01",
            "try confidential documents. Your\x01",
            "practice mission today is to retrieve them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#4P#1004FWait. 'Confidential' stuff? Seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#6P#840FHaha! Well, it's more to get you\x01",
            "'in the mood' than anything else.\x02\x03",

            "Regardless. The documents are in\x01",
            "the deepest section of the sewers.\x02\x03",

            "Recover them, and today's\x01",
            "practice will be complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#6P#816FWell, you make it sound easy,\x01",
            "buuuuuuut...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#4P#1006FThis is a training mission,\x01",
            "so you've made sure it isn't\x01",
            "gonna be that easy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#6P#843FI shall leave that to your doubtlessly\x01",
            "fertile imaginations.\x02\x03",

            "#842FI will warn you, however: the monsters in\x01",
            "the channel are not to be underestimated.\x02\x03",

            "You may find it necessary to fully\x01",
            "master Chain Crafts to defeat them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#4P#1004FChain Crafts, right.\x01",
            "Those are the, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10A,
        (
            "#6P#812FYou mean the team-based attacks\x01",
            "we got special training for, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#6P#840FIndeed. Fundamentally, it is a type\x01",
            "of craft which allows several people\x01",
            "to attack a target simultaneously.\x02\x03",

            "You've put a great deal of effort\x01",
            "into learning them, so now you\x01",
            "should put theory into practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#4P#1006FSounds like a plan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#6P#840FAh, also, since you'll be fighting once\x01",
            "again, let me provide you with this.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #15
        "Received the #2CMonster Guide#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x20F, 1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #16
        0x101,
        "#1011FOh, hey, this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        (
            "#6P#816FThat's one of those Monster\x01",
            "Guide thingies, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#841FCorrect. It's a notebook for recording\x01",
            "information about any foes you might\x01",
            "come to face.\x02\x03",

            "#840FI would advise noting down any particulars\x01",
            "about your enemies as you find them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1006FWell, keeping tabs on the enemy IS\x01",
            "how you win fights, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10A,
        (
            "#810FYeah! They say knowing your enemy\x01",
            "is the first key to victory! Or is it, uh,\x01",
            "know yourself first...?\x02\x03",

            "#811FUh, either way! Thanks, Kurt.\x01",
            "We really owe you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#840FReally, there's no need to thank me.\x01",
            "I wish you two the best of luck.\x02\x03",

            "As one last note, if I may... Don't force\x01",
            "yourself to go on if you are injured.\x02\x03",

            "I've prepared an orbment charging station\x01",
            "here, just in case. Use it as you see fit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1008FYep, that's our Kurt, all right.\x01",
            "Always planning for everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#810FWell, no excuses now! Time to blow\x01",
            "the lid off the pot of expectations!\x02\x03",

            "#1310FAll right, let's get to it!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x5)
    OP_10(0x0, 0x0)
    OP_A2(0x1009)
    OP_28(0x7E, 0x4, 0x2)
    OP_28(0x7E, 0x4, 0x8)
    OP_28(0x7E, 0x1, 0x80)
    ClearChrFlags(0x8, 0x40)
    EventEnd(0x0)
    Return()

    # Function_4_6AC end

    def Function_5_1231(): pass

    label("Function_5_1231")

    OP_8E(0x8, 0xFFFFFCFE, 0x0, 0x1D1A, 0x7D0, 0x0)
    OP_8C(0x8, 170, 500)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Return()

    # Function_5_1231 end

    def Function_6_1254(): pass

    label("Function_6_1254")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_1272")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1283")

    label("loc_1272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_END)), "loc_1283")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1283")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1601")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_131F"),
        (1, "loc_134B"),
        (2, "loc_138C"),
        (SWITCH_DEFAULT, "loc_13E0"),
    )


    label("loc_131F")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",          # 0
            "[Balstar Channel]\x01",      # 1
        )
    )

    Jump("loc_13E0")

    label("loc_134B")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
        )
    )

    Jump("loc_13E0")

    label("loc_138C")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
            "[Grimsel Fortress]\x01",        # 3
        )
    )

    Jump("loc_13E0")

    label("loc_13E0")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_140A"),
        (1, "loc_1483"),
        (2, "loc_1500"),
        (3, "loc_1580"),
        (SWITCH_DEFAULT, "loc_15FE"),
    )


    label("loc_140A")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #24
        "\x07\x05Move to [Guild Lodge]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1470"),
        (1, "loc_147D"),
        (SWITCH_DEFAULT, "loc_1480"),
    )


    label("loc_1470")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1480")

    label("loc_147D")

    Jump("loc_1480")

    label("loc_1480")

    Jump("loc_15FE")

    label("loc_1483")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #25
        "\x07\x05Move to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14ED"),
        (1, "loc_14FA"),
        (SWITCH_DEFAULT, "loc_14FD"),
    )


    label("loc_14ED")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14FD")

    label("loc_14FA")

    Jump("loc_14FD")

    label("loc_14FD")

    Jump("loc_15FE")

    label("loc_1500")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #26
        "\x07\x05Move to [Saint-Croix Forest]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_156D"),
        (1, "loc_157A"),
        (SWITCH_DEFAULT, "loc_157D"),
    )


    label("loc_156D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_157D")

    label("loc_157A")

    Jump("loc_157D")

    label("loc_157D")

    Jump("loc_15FE")

    label("loc_1580")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #27
        "\x07\x05Move to [Grimsel Fortress]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15EB"),
        (1, "loc_15F8"),
        (SWITCH_DEFAULT, "loc_15FB"),
    )


    label("loc_15EB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15FB")

    label("loc_15F8")

    Jump("loc_15FB")

    label("loc_15FB")

    Jump("loc_15FE")

    label("loc_15FE")

    Jump("loc_12F4")

    label("loc_1601")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_161A"),
        (1, "loc_164E"),
        (2, "loc_1682"),
        (3, "loc_16B6"),
        (SWITCH_DEFAULT, "loc_16EA"),
    )


    label("loc_161A")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_16EA")

    label("loc_164E")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_16EA")

    label("loc_1682")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_16EA")

    label("loc_16B6")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_16EA")

    label("loc_16EA")

    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_171B"),
        (1, "loc_1727"),
        (2, "loc_1733"),
        (3, "loc_173F"),
        (SWITCH_DEFAULT, "loc_174B"),
    )


    label("loc_171B")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_174B")

    label("loc_1727")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_174B")

    label("loc_1733")

    NewScene("ED6_DT21/C5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_174B")

    label("loc_173F")

    NewScene("ED6_DT21/C5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_174B")

    label("loc_174B")

    Return()

    # Function_6_1254 end

    def Function_7_174C(): pass

    label("Function_7_174C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_END)), "loc_1754")
    Return()

    label("loc_1754")

    EventBegin(0x0)
    SetChrPos(0x8, 10060, 0, 201910, 270)
    OP_44(0x8, 0x0)
    SetChrSubChip(0x8, 0)

    NpcTalk(    #28
        0x8,
        "Man's Voice",
        (
            "Ah, very good.\x01",
            "You finally found your way down here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 1000)
    TurnDirection(0x10A, 0x8, 1000)

    def lambda_17FD():
        OP_6D(8550, 0, 201870, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17FD)

    def lambda_1815():
        OP_67(0, 6500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1815)

    def lambda_182D():
        OP_6C(89000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_182D)

    def lambda_183D():
        OP_6B(3150, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_183D)
    Sleep(2000)
    SetChrPos(0x10A, -3580, 0, 200950, 90)
    SetChrPos(0x101, -3660, 0, 202230, 90)

    def lambda_1874():
        OP_8E(0x101, 0x18F6, 0x0, 0x31786, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1874)
    Sleep(200)

    def lambda_1894():
        OP_8E(0x10A, 0x17DE, 0x0, 0x311F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1894)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x10A, 0x1)

    ChrTalk(    #29
        0x10A,
        "#814F#2PK-Kurt?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1004F#1PHang on a second...\x02\x03",

            "You were at the entrance!\x01",
            "How'd you get here before us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#841FTo tell you the truth...there are a few\x01",
            "secret passages through the channel.\x02\x03",

            "While you worked your way down the\x01",
            "'main' path, I simply came here directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1007F#1PAww, man...\x02\x03",

            "#1019FNow all the hard work we put into\x01",
            "beating those monsters and stuff\x01",
            "feels like a waste. Thanks, Kurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10A,
        (
            "#812F#2PAaanyway, busy work aside...\x02\x03",

            "Isn't this as deep as the sewers go?\x01",
            "This is the end of the line, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "#840FQuite so. Your point?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10A,
        (
            "#819F#2PSo, uh, the 'confidential documents'\x01",
            "are...um...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        "#841FHeh...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 2)
    OP_0D()
    Sleep(500)
    OP_62(0x10A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1B71():
        OP_91(0x101, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B71)
    Sleep(100)

    def lambda_1B91():
        OP_91(0x10A, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1B91)
    WaitChrThread(0x10A, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(200)

    ChrTalk(    #37
        0x101,
        "#1020F#1PWh-What's with the...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        "#1316F#2POhhhhh man. I knew it, I knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#845FI am afraid my role in this exercise\x01",
            "is that of an armed foreign infiltrator,\x01",
            "here to steal the documents.\x02\x03",

            "As we have the same goal, my only\x01",
            "option is to remove you...by force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1005F#1PWait, WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10A,
        (
            "#815F#2PThe documents were just\x01",
            "an excuse to get us here...\x02\x03",

            "The REAL point of the test is to have\x01",
            "an unexpected battle during a mission,\x01",
            "isn't it?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#841FIndeed. Well spotted, Anelace.\x02\x03",

            "#846FThat being said... Prepare yourselves!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)
    Battle(0x393, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1DF1"),
        (SWITCH_DEFAULT, "loc_1DF6"),
    )


    label("loc_1DF1")

    OP_B4(0x0)
    Jump("loc_1DF6")

    label("loc_1DF6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    OP_44(0x8, 0x0)
    OP_6C(45000, 0)
    SetChrPos(0x8, 10060, 0, 201910, 270)
    SetChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 3)
    SetChrPos(0x101, 6350, 0, 202970, 92)
    SetChrChipByIndex(0x101, 5)
    SetChrPos(0x10A, 6350, 0, 200970, 92)
    SetChrChipByIndex(0x10A, 6)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #43
        0x8,
        (
            "#843FWhew. I wasn't even holding back that time.\x02\x03",

            "Well done. That was a clean victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1003F*pant pant*\x02\x03",

            "We... We won?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        (
            "#813F#6PY-Yeah... My arms say otherwise,\x01",
            "but we did...\x02\x03",

            "Just what you'd expect from the Artful Tactician.\x01",
            "Two on one and we barely won...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #46
        0x8,
        (
            "#841FAll right. With the infiltrator neutralized,\x01",
            "the documents have been recovered.\x02\x03",

            "This mission is complete.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Sleep(100)
    SetChrChipByIndex(0x10A, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(    #47
        0x101,
        "#1011FOkay, so training for today is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10A,
        "#1310F#6PIs...over...rrrrright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#840FOh, hardly.\x02\x03",

            "After a brief lunch at the inn, we'll be heading\x01",
            "to the Saint-Croix Forest to the south.\x02\x03",

            "We will engage in a bit of 'bonus training'\x01",
            "there. Think of it as a chance to make up\x01",
            "for any mistakes you made here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #50
        0x101,
        "#1007FOh, boy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        "#1316F#6PKuuuurt...come on, cut us some slack here!\x02",
    )

    CloseMessageWindow()
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    NewScene("ED6_DT21/T5101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_174C end

    def Function_8_21FE(): pass

    label("Function_8_21FE")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    Return()

    # Function_8_21FE end

    def Function_9_2227(): pass

    label("Function_9_2227")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #52
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_2227 end

    def Function_10_2276(): pass

    label("Function_10_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 0)), scpexpr(EXPR_END)), "loc_227E")
    Return()

    label("loc_227E")

    EventBegin(0x0)
    TurnDirection(0x0, 0x9, 0)
    TurnDirection(0x1, 0x9, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_229C")
    Call(0, 11)
    Jump("loc_271A")

    label("loc_229C")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x101,
        "#1002FMonsters already? That was quick.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10A,
        (
            "#810FI'll say! These'll be perfect\x01",
            "for a warm-up, though!\x02\x03",

            "Oh, yeah, this is our first real fight in\x01",
            "a while, isn't it? Might be worth it to\x01",
            "go over the basics of fighting again...\x02\x03",

            "Well, how about it, Estelle?\x02\x03",

            "Wanna go over everything again, or skip\x01",
            "straight to the, ah, 'practical stuff'?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Go Over Everything\x01",      # 0
            "Just Chain Crafts\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x101, 0x10A, 400)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2481"),
        (1, "loc_255F"),
        (SWITCH_DEFAULT, "loc_265B"),
    )


    label("loc_2481")


    ChrTalk(    #55
        0x101,
        (
            "#1015FHmm... Maybe we ought to go\x01",
            "over the basics again.\x02\x03",

            "Like you said, it's been a while\x01",
            "since we've fought real monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10A,
        (
            "#816FFair enough! From the top, then!\x02\x03",

            "C'mon, Estelle! Follow me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1018FRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_265B")

    label("loc_255F")

    OP_A2(0x1064)

    ChrTalk(    #58
        0x101,
        (
            "#1015FCan we skip straight to the 'practical' stuff?\x02\x03",

            "I kinda want to try out these Chain\x01",
            "Crafts we've been practicing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10A,
        (
            "#816FHeheh! Music to my ears!\x02\x03",

            "All right, then! Let's plow through\x01",
            "these critters, double-time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#1018FRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_265B")

    label("loc_265B")

    OP_59()
    OP_A2(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_2716")
    OP_A2(0x1160)
    OP_A2(0x1161)
    OP_A2(0x1162)
    FadeToDark(500, 0, -1)

    def lambda_267F():
        OP_69(0x9, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_267F)

    def lambda_268D():
        OP_8E(0x0, 0xFFFFC9B4, 0x0, 0x4A24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_268D)

    def lambda_26A8():
        OP_8E(0x1, 0xFFFFC9B4, 0x0, 0x4A24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_26A8)
    OP_0D()
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x0)
    OP_44(0x1, 0x0)
    SetChrPos(0x0, -36020, 0, 38300, 0)
    SetChrPos(0x1, -36020, 0, 38300, 0)
    OP_69(0x0, 0x0)
    OP_4A(0x0, 0)
    OP_4A(0x1, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Sleep(4000)
    Call(0, 18)
    Jump("loc_271A")

    label("loc_2716")

    Call(0, 11)

    label("loc_271A")

    EventEnd(0x0)
    Return()

    # Function_10_2276 end

    def Function_11_271D(): pass

    label("Function_11_271D")

    OP_59()

    def lambda_2724():
        OP_69(0x9, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2724)

    def lambda_2732():
        OP_8E(0x0, 0xFFFFC9B4, 0x0, 0x4A24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2732)

    def lambda_274D():
        OP_8E(0x1, 0xFFFFC9B4, 0x0, 0x4A24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_274D)
    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Battle(0x11, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2788"),
        (SWITCH_DEFAULT, "loc_29C0"),
    )


    label("loc_2788")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    EventBegin(0x0)
    SetChrPos(0x101, -13420, 0, 18940, 0)
    SetChrPos(0x10A, -14920, 0, 18970, 0)
    OP_6D(-14170, 400, 18970, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #61
        0x101,
        "#1018FOkay, that wasn't too hard!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #62
        0x10A,
        (
            "#810FYeah, great work, Estelle!\x02\x03",

            "Oh, but, one thing. We oughtta put\x01",
            "those things in the Monster Guide!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #63
        0x101,
        (
            "#1006FOh, right.\x01",
            "No problem, give me a sec...\x02\x03",

            "#1029F*confident penciling*\x02\x03",

            "#1006FOkay, got it all down!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #64
        (
            "\x07\x05Information about enemies fought will be automatically recorded in\x01",
            "your Monster Guide.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #65
        (
            "\x07\x05Note that recorded information may change depending on whether\x01",
            "you are victorious or flee from battle.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_29C0")

    label("loc_29C0")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Return()

    # Function_11_271D end

    def Function_12_29C9(): pass

    label("Function_12_29C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 1)), scpexpr(EXPR_END)), "loc_29D1")
    Return()

    label("loc_29D1")

    EventBegin(0x0)
    TurnDirection(0x0, 0xA, 0)
    TurnDirection(0x1, 0xA, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C2F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x46)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x46)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B61")

    ChrTalk(    #66
        0x10A,
        (
            "#814FOh, Estelle, do you have some\x01",
            "attack arts ready?\x02\x03",

            "#810FWe should get those set\x01",
            "up before we go any further.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #67
        (
            "\x07\x05Quartz set-up is done from the Orbment menu. To open the\x01",
            "Orbment menu, select the 'Orbment' tab from the main menu.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    EventEnd(0x0)
    Return()

    label("loc_2B61")


    ChrTalk(    #68
        0x10A,
        (
            "#810FArts work really well against\x01",
            "some enemies that you can't hurt\x01",
            "much with normal weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1006FGot it. So we just use arts against\x01",
            "those monsters, right?\x02\x03",

            "Okay then, let's keep going.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 13)
    Jump("loc_30FB")

    label("loc_2C2F")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x101,
        "#1002FUh oh, here come some more.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x46)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x46)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EEB")

    ChrTalk(    #71
        0x10A,
        (
            "#1316FEuuuugh, these things are all sludgy\x01",
            "and soft. My sword's a toothpick\x01",
            "against them, and so is your staff.\x02\x03",

            "#812FThis is a perfect chance to whip\x01",
            "out some arts, although...\x02\x03",

            "Estelle, you do have some set, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1015FI, uh...might? Maybe?\x02\x03",

            "Lemme double check my orbment...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #73
        0x10A,
        (
            "#810FOkay, let's go forward once you're\x01",
            "sure your orbment is all set up.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #74
        (
            "\x07\x05Quartz set-up is done from the Orbment menu. To open the\x01",
            "Orbment menu, select the 'Orbment' tab from the main menu.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    EventEnd(0x0)
    Return()

    label("loc_2EEB")


    ChrTalk(    #75
        0x10A,
        (
            "#1316FEuuuugh, these things are all sludgy\x01",
            "and soft. My sword's a toothpick\x01",
            "against them, and so is your staff.\x02\x03",

            "#810FThis is a perfect chance to whip out some arts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1006FSo just blow these monsters\x01",
            "up with arts, right?\x02\x03",

            "Okay then, here we go!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #77
        (
            "\x07\x05Arts can prove effective against enemies where default attacks do\x01",
            "not. Arts can be cast over long ranges but take time to activate.\x02\x03",

            "Using arts consumes EP. To recharge EP, rest at an inn, hotel,\x01",
            "or recovery point, or use EP Charge items.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1)
    Call(0, 13)

    label("loc_30FB")

    EventEnd(0x3)
    Return()

    # Function_12_29C9 end

    def Function_13_30FE(): pass

    label("Function_13_30FE")

    OP_59()

    def lambda_3105():
        OP_69(0xA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3105)

    def lambda_3113():
        OP_8E(0x0, 0xFFFF9AD4, 0x0, 0x6CDE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3113)

    def lambda_312E():
        OP_8E(0x1, 0xFFFF9AD4, 0x0, 0x6CDE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_312E)
    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Battle(0x12, 0x0, 0x0, 0x0, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Return()

    # Function_13_30FE end

    def Function_14_3166(): pass

    label("Function_14_3166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 2)), scpexpr(EXPR_END)), "loc_316E")
    Return()

    label("loc_316E")

    EventBegin(0x0)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_318C")
    Call(0, 15)
    Jump("loc_3537")

    label("loc_318C")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x101,
        "#1007FGood grief, another group already?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #79
        0x10A,
        (
            "#816FWell, this is a pretty good chance\x01",
            "to practice crafts, Estelle.\x02\x03",

            "Remember, crafts aren't just attacks--\x01",
            "They have all kinds of effects, depending\x01",
            "on what you do!\x02\x03",

            "And if you can get 100 CP, you can\x01",
            "break out a super-strong S-Craft!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #80
        0x101,
        (
            "#1011FOkay, I see...\x02\x03",

            "Crafts are pretty important for giving\x01",
            "yourself tactical options, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10A,
        (
            "#816FYep! And remember, using S-Breaks\x01",
            "to get an S-Craft in quick is important\x01",
            "in real combat!\x02\x03",

            "We'll go over S-Breaks in the actual\x01",
            "fight, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1006FOkay! Let's do this, Anelace!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #83
        (
            "\x07\x05Crafts have similar range limitations to physical attacks, but occur\x01",
            "immediately. CP, which is used to activate crafts, is gained when\x01",
            "dealing or receiving damage.\x02\x03",

            "Should your CP reach over 100, you will be able to use a special\x01",
            "craft, an S-Craft, and you can also trigger an S-Break.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2)
    Call(0, 15)

    label("loc_3537")

    EventEnd(0x3)
    Return()

    # Function_14_3166 end

    def Function_15_353A(): pass

    label("Function_15_353A")

    OP_59()

    def lambda_3541():
        OP_69(0xB, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3541)

    def lambda_354F():
        OP_8E(0x0, 0xFFFF72E8, 0x0, 0x83A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_354F)

    def lambda_356A():
        OP_8E(0x1, 0xFFFF72E8, 0x0, 0x83A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_356A)
    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Battle(0x13, 0x0, 0x0, 0x0, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Return()

    # Function_15_353A end

    def Function_16_35A2(): pass

    label("Function_16_35A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22C, 3)), scpexpr(EXPR_END)), "loc_35AA")
    Return()

    label("loc_35AA")

    EventBegin(0x0)
    TurnDirection(0x0, 0xC, 0)
    TurnDirection(0x1, 0xC, 0)
    OP_35(0x0, 0x8C)
    OP_35(0x9, 0x8C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_366F")

    ChrTalk(    #84
        0x10A,
        (
            "#810FHey, if we get the chance,\x01",
            "let's try to start a Chain Craft.\x02\x03",

            "I mean, come on, it's a new kind\x01",
            "of attack. I wanna try it out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#1006FOkay, sure!\x02",
    )

    CloseMessageWindow()
    Call(0, 17)
    Jump("loc_3855")

    label("loc_366F")


    ChrTalk(    #86
        0x101,
        (
            "#1011FLooks like this is\x01",
            "the end of the path...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10A,
        (
            "#810FYeah, looks like. Althoooough...\x02\x03",

            "Hey, Estelle. Think we can\x01",
            "finally give it a shot?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #88
        0x101,
        (
            "#1011F#3PUh...'It'?\x02\x03",

            "#1018FOh, you mean a Chain Craft, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #89
        0x10A,
        (
            "#1310FHeehee! Well, we did put a lot of\x01",
            "sweat into learning these new chain\x01",
            "attacks, y'know.\x02\x03",

            "I say we try 'em out in a real fight\x01",
            "and get a feel for how they work in\x01",
            "practice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1006F#3PWorks for me! C'mon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10A,
        "#810FRight! Just say when!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x3)
    Call(0, 17)

    label("loc_3855")

    EventEnd(0x0)
    Return()

    # Function_16_35A2 end

    def Function_17_3858(): pass

    label("Function_17_3858")

    OP_59()

    def lambda_385F():
        OP_69(0xC, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_385F)

    def lambda_386D():
        OP_8E(0x0, 0xFFFF728E, 0x0, 0xB6B2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_386D)

    def lambda_3888():
        OP_8E(0x1, 0xFFFF728E, 0x0, 0xB6B2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3888)
    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Battle(0x10, 0x0, 0x0, 0x0, 0xFF)
    OP_72(0x1, 0x800)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_71(0x1, 0x800)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_3BD6")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_38EF"),
        (SWITCH_DEFAULT, "loc_3BD6"),
    )


    label("loc_38EF")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    EventBegin(0x0)
    SetChrPos(0x101, -35600, 0, 44540, 0)
    SetChrPos(0x10A, -37100, 0, 44540, 0)
    OP_6D(-36350, 400, 44540, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #92
        0x101,
        (
            "#1018FPiece of cake!\x02\x03",

            "#1004FOh, right, while we're at it...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #93
        0x10A,
        "#814FWhat's up, Estelle?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #94
        0x101,
        (
            "#1016FWell, the Monster Guide. Best to\x01",
            "record what we learned as soon\x01",
            "as possible after the fight, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10A,
        (
            "#818FOh, yeah, good thinking.\x01",
            "I was, uh, totally gonna suggest that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1006FJust gimme a second.\x01",
            "I'll write this up real quick...\x02\x03",

            "#1029F*confident penciling*\x02\x03",

            "#1006FOkay, got it all down!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #97
        (
            "\x07\x05Information about enemies fought will be automatically recorded in\x01",
            "your Monster Guide.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #98
        (
            "\x07\x05Note that recorded information may change depending on whether\x01",
            "you are victorious or flee from battle.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_3BD6")

    label("loc_3BD6")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Return()

    # Function_17_3858 end

    def Function_18_3BDF(): pass

    label("Function_18_3BDF")

    EventBegin(0x0)
    OP_6D(-26300, 0, 26230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(11000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -36520, 0, 36440, 0)
    SetChrPos(0xF7, -35650, 0, 35240, 0)

    def lambda_3C46():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3C46)
    Sleep(250)

    def lambda_3C61():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3C61)

    def lambda_3C77():
        OP_6D(-36080, 0, 43850, 4500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3C77)

    def lambda_3C8F():
        OP_6C(45000, 4500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3C8F)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    Sleep(1000)
    OP_35(0x0, 0x8C)
    OP_35(0x9, 0x8C)

    ChrTalk(    #99
        0x101,
        (
            "#1015F#1PWell, so much for the monsters, but...\x02\x03",

            "#1011FThis kinda looks like the end of the path...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10A,
        (
            "#810FYeah, looks like. Althoooough...\x02\x03",

            "Hey, Estelle. Think we can\x01",
            "finally give it a shot?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #101
        0x101,
        (
            "#1011F#1PUh...'It'?\x02\x03",

            "#1018FOh, you mean a Chain Craft, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #102
        0x10A,
        (
            "#1310FHeehee! Well, we did put a lot of\x01",
            "sweat into learning these new chain\x01",
            "attacks, y'know.\x02\x03",

            "I say we try 'em out in a real fight\x01",
            "and get a feel for how they work in\x01",
            "practice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1006F#1PWorks for me! C'mon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10A,
        "#816FRight! Just say when!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_3EDD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3EDD)
    OP_8C(0x101, 0, 400)
    OP_A2(0x3)
    OP_6A(0xFF)
    Call(0, 17)
    Return()

    # Function_18_3BDF end

    def Function_19_3EF7(): pass

    label("Function_19_3EF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F5D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #105
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_4118")

    label("loc_3F5D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #106
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40FD")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, -5000, 1000, 6730, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x32)
    OP_73(0x2)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -5000, 1000, 6730, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, -5000, 1000, 6730, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x2, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_40FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4117")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_4117")

    Return()

    label("loc_4118")

    Return()

    # Function_19_3EF7 end

    SaveToFile()

Try(main)
