from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4402   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Phelio',                               # 9
        'Royal Army Soldier',                   # 10
        'Maintenance Chief Gustav',             # 11
        'Faye',                                 # 12
        'Sandon',                               # 13
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH02440 ._CH',             # 02
        'ED6_DT07/CH01550 ._CH',             # 03
        'ED6_DT07/CH01530 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH02440P._CP',             # 02
        'ED6_DT07/CH01550P._CP',             # 03
        'ED6_DT07/CH01530P._CP',             # 04
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 540,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 1520,
        Z                   = 0,
        Y                   = 9460,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 3010,
        Z                   = 0,
        Y                   = 400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 2520,
        Z                   = 0,
        Y                   = 9450,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 6550,
        Z                   = 0,
        Y                   = 11890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = 1050,
        TriggerZ            = 0,
        TriggerY            = 7890,
        TriggerRange        = 800,
        ActorX              = 150,
        ActorZ              = 1700,
        ActorY              = 7890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1050,
        TriggerZ            = 0,
        TriggerY            = 10640,
        TriggerRange        = 800,
        ActorX              = 150,
        ActorZ              = 1700,
        ActorY              = 10640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1720,
        TriggerZ            = 0,
        TriggerY            = 540,
        TriggerRange        = 600,
        ActorX              = 500,
        ActorZ              = 1500,
        ActorY              = 540,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_20B",          # 01, 1
        "Function_2_274",          # 02, 2
        "Function_3_3F1",          # 03, 3
        "Function_4_3F6",          # 04, 4
        "Function_5_17B0",         # 05, 5
        "Function_6_1876",         # 06, 6
        "Function_7_19F0",         # 07, 7
        "Function_8_1BD8",         # 08, 8
        "Function_9_1DD0",         # 09, 9
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1F9")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_20A")

    label("loc_1F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_20A")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_20A")

    Return()

    # Function_0_1DE end

    def Function_1_20B(): pass

    label("Function_1_20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B")
    OP_B1("t4402_y")
    Jump("loc_234")

    label("loc_22B")

    OP_B1("t4402_n")

    label("loc_234")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_255")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    Jump("loc_273")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_273")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)

    label("loc_273")

    Return()

    # Function_1_20B end

    def Function_2_274(): pass

    label("Function_2_274")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3DB")

    label("loc_299")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3DB")

    label("loc_2B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3DB")

    label("loc_2CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3DB")

    label("loc_2E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3DB")

    label("loc_2FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3DB")

    label("loc_316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3DB")

    label("loc_32F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3DB")

    label("loc_348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3DB")

    label("loc_361")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3DB")

    label("loc_37A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_393")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3DB")

    label("loc_393")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3DB")

    label("loc_3AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3DB")

    label("loc_3C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3DB")

    label("loc_3F0")

    Return()

    # Function_2_274 end

    def Function_3_3F1(): pass

    label("Function_3_3F1")

    Call(0, 4)
    Return()

    # Function_3_3F1 end

    def Function_4_3F6(): pass

    label("Function_4_3F6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_409")
    OP_A2(0x0)
    Jump("loc_41F")

    label("loc_409")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x80)"), scpexpr(EXPR_END)), "loc_419")
    OP_A2(0x1)
    Jump("loc_41F")

    label("loc_419")

    OP_A3(0x0)
    OP_A3(0x1)

    label("loc_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Completed QST104\x01",            # 0
            "Failed QST104\x01",               # 1
            "Time ran out on QST104\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_495"),
        (1, "loc_49B"),
        (2, "loc_4A1"),
        (SWITCH_DEFAULT, "loc_4AA"),
    )


    label("loc_495")

    OP_A2(0x0)
    Jump("loc_4AA")

    label("loc_49B")

    OP_A2(0x1)
    Jump("loc_4AA")

    label("loc_4A1")

    OP_A3(0x0)
    OP_A3(0x1)
    Jump("loc_4AA")

    label("loc_4AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_704")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_701")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_54D")

    ChrTalk(    #0
        0x8,
        (
            "I promised my wife I wouldn't get\x01",
            "involved with gambling again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "More to the point, the airships\x01",
            "aren't even working, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_701")

    label("loc_54D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_634")

    ChrTalk(    #2
        0x8,
        (
            "...Ruan's casino didn't use any\x01",
            "orbments, did it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "If I've gotta work, then I might as\x01",
            "well go on a casino vacation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Wait, no, I'm an idiot! Bad thoughts!\x01",
            "BAAAAD THOUGHTS!\x01",
            "I promised I'd stop gambling!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_701")

    label("loc_634")


    ChrTalk(    #5
        0x8,
        (
            "Thanks to this strange phenomenon,\x01",
            "we can't contact Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "We have no way of knowing\x01",
            "when ships will arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "...So if the orbments have stopped,\x01",
            "does that mean the ships have\x01",
            "stopped too?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_701")

    Jump("loc_17AC")

    label("loc_704")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_A94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 5)), scpexpr(EXPR_END)), "loc_7E8")

    ChrTalk(    #8
        0x8,
        (
            "We're cooperating with the army\x01",
            "from here on out to avoid another\x01",
            "disaster with the engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "Can't imagine how anyone would\x01",
            "get their hands on those babies\x01",
            "now before the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A91")

    label("loc_7E8")


    ChrTalk(    #10
        0x8,
        (
            "Oh, hey! I remember you guys.\x01",
            "Bracers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1000FYeah, we just came to check\x01",
            "up on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "Well, thanks to you, the new\x01",
            "model engine sample is back\x01",
            "safe and sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "I really appreciate it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8E5")

    ChrTalk(    #14
        0x106,
        "#050FHow's guard duty goin'?\x02",
    )

    CloseMessageWindow()
    Jump("loc_905")

    label("loc_8E5")


    ChrTalk(    #15
        0x103,
        "#020FIs the security okay?\x02",
    )

    CloseMessageWindow()

    label("loc_905")


    ChrTalk(    #16
        0x8,
        (
            "We're not taking any more chances.\x01",
            "Ever since what happened, we've\x01",
            "enlisted the Royal Army's help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "These components are a big enough\x01",
            "deal to make or break the pact, so it\x01",
            "only makes sense to get them involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "If there's anything you guys'd \x01",
            "like to leave in the warehouses,\x01",
            "by the way, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1000FAhaha, if the chance comes up,\x01",
            "we might take you up on that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1655)

    label("loc_A91")

    Jump("loc_17AC")

    label("loc_A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_BB3")

    ChrTalk(    #20
        0x8,
        (
            "The samples of the new model\x01",
            "engines will be stored here until\x01",
            "the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "This was a warehouse before\x01",
            "it became an office, so it's got \x01",
            "room for a couple of engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "Plus there's always someone\x01",
            "at the front desk, so security\x01",
            "will be 'round the clock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AC")

    label("loc_BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_D7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C4F")

    ChrTalk(    #23
        0x8,
        (
            "My wife delivered a boxed\x01",
            "lunch for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "I've got my fair share of night\x01",
            "shifts ahead of me, so here's\x01",
            "hoping I can pull through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7B")

    label("loc_C4F")


    ChrTalk(    #25
        0x8,
        (
            "My wife delivered a boxed\x01",
            "lunch for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "She still cares about me even\x01",
            "after everything I've put her through...\x01",
            "*sniffle*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "We're going to be storing\x01",
            "some real important stuff in\x01",
            "here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "I've got my fair share of night\x01",
            "shifts ahead of me, so here's\x01",
            "hoping I can pull through.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_D7B")

    Jump("loc_17AC")

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_122C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E99")

    ChrTalk(    #29
        0x8,
        (
            "Thinking about it, I've caused\x01",
            "some real trouble for my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "Moving to the capital even though we don't\x01",
            "have much money, getting involved in gambling\x01",
            "and losing what little we did have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "Things can't keep going this way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F8A")

    label("loc_E99")


    ChrTalk(    #32
        0x8,
        (
            "Man, my wife's gotten a lot\x01",
            "more strict lately. It's like she's\x01",
            "a different person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "I'd accidentally slept in a bit\x01",
            "this morning, and that got me\x01",
            "kicked out in my pajamas!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "I think...I awoke a sleeping Rhinocider.\x01",
            "*shudder*\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_F8A")

    Jump("loc_1197")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1051")

    ChrTalk(    #35
        0x8,
        (
            "I dragged my wife along pretty\x01",
            "hard on that casino vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "...But me dragging her around is\x01",
            "nothing new.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "Thinking about it, I've been nothing\x01",
            "but trouble for my wife...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1197")

    label("loc_1051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10F1")

    ChrTalk(    #38
        0x8,
        (
            "This office here manages work\x01",
            "in the harbor block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "We'll take orders for transport\x01",
            "on freight ships and use of the\x01",
            "rental warehouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1197")

    label("loc_10F1")


    ChrTalk(    #40
        0x8,
        "Oh, customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "This office here manages\x01",
            "work in the harbor block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "We'll take orders for transport\x01",
            "on freight ships and use of the\x01",
            "rental warehouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1197")

    Jump("loc_1229")

    label("loc_119A")


    ChrTalk(    #43
        0x8,
        (
            "This office here manages\x01",
            "work in the harbor block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "We'll take orders for transport\x01",
            "on freight ships and use of the\x01",
            "rental warehouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1229")

    Jump("loc_17AC")

    label("loc_122C")


    ChrTalk(    #45
        0x8,
        (
            "Oh? It's rare to see customers\x01",
            "come without an appointment...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_140D")

    ChrTalk(    #46
        0x8,
        "Hey!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "You're the people who beat me\x01",
            "at the casino in Ruan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1004FAh...\x02\x03",

            "#1001FAhahaha...\x01",
            "Nice to see you too, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "*siiigh* Listen, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "After that, I tried making up\x01",
            "for the money I'd lost with all\x01",
            "kindsa gambles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "...that match with you\x01",
            "was where my luck turned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "When I realized everything\x01",
            "I'd won had disappeared,\x01",
            "well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AB")

    label("loc_140D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15AB")

    ChrTalk(    #53
        0x8,
        "Hey!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "You're the people who challenged\x01",
            "me back at the casino in Ruan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1004FAh...\x02\x03",

            "#1008FAhahaha...\x01",
            "Nice to see you too, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        "Maaan, you gotta listen to this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "After I won against you, I got\x01",
            "overconfident and tried playing\x01",
            "this girl who works there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "But--and wouldn't you know it!--\x01",
            "my luck ran out with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "When I realized everything\x01",
            "I'd won had disappeared,\x01",
            "well...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AB")


    ChrTalk(    #60
        0x101,
        "#1004FR-Really? That's kinda sad.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1652")

    ChrTalk(    #61
        0x104,
        (
            "#035FGambling for riches is naught but\x01",
            "a fleeting dream of a single night,\x01",
            "destined never to come true...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16BB")

    label("loc_1652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_167E")

    ChrTalk(    #62
        0x106,
        "#051FThat's gamblin' for ya.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16BB")

    label("loc_167E")


    ChrTalk(    #63
        0x103,
        (
            "#021FThat's what gambling is,\x01",
            "when you cut right to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BB")


    ChrTalk(    #64
        0x8,
        (
            "Yeah, if only I'd figured it out\x01",
            "sooner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "I guess it's true of anything,\x01",
            "but you should always know\x01",
            "when to quit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "I didn't, and I made things hard for\x01",
            "my wife because of that. I'm\x01",
            "gonna do all I can to make it up to her.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1654)
    OP_A2(0x2)

    label("loc_17AC")

    TalkEnd(0x8)
    Return()

    # Function_4_3F6 end

    def Function_5_17B0(): pass

    label("Function_5_17B0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1872")

    ChrTalk(    #67
        0xFE,
        (
            "Under Colonel Cid's orders,\x01",
            "we're working as security detail\x01",
            "for the engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "The last thing we want is for\x01",
            "problems to arise with the signing\x01",
            "ceremony due to another theft.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1872")

    TalkEnd(0x9)
    Return()

    # Function_5_17B0 end

    def Function_6_1876(): pass

    label("Function_6_1876")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_19EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_18F1")

    ChrTalk(    #69
        0xFE,
        (
            "#691FWe're gonna head on back\x01",
            "once this guy here stamps\x01",
            "our forms.\x02\x03",

            "Good luck with your own work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19EC")

    label("loc_18F1")


    ChrTalk(    #70
        0xFE,
        (
            "#692FOh, hey, everyone.\x02\x03",

            "#691FWe just finished carryin'\x01",
            "the samples in.\x02\x03",

            "The plan is that they'll be\x01",
            "stored here until the day of\x01",
            "the signing ceremony.\x02\x03",

            "We'll be heading back\x01",
            "once this guy here stamps\x01",
            "our forms.\x02\x03",

            "Good luck with your own work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_19EC")

    TalkEnd(0xA)
    Return()

    # Function_6_1876 end

    def Function_7_19F0(): pass

    label("Function_7_19F0")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_1BD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1AAD")

    ChrTalk(    #71
        0xFE,
        (
            "The engineers here put their\x01",
            "hearts and souls into making\x01",
            "these engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I know I suck at expressing\x01",
            "my feelings, but...I don't want\x01",
            "anything to cheapen that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD4")

    label("loc_1AAD")


    ChrTalk(    #73
        0xFE,
        (
            "Hmm, didn't think we'd be\x01",
            "givin' em away for free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "It's not that I want us to get\x01",
            "something back for 'em, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "The engineers here put their\x01",
            "hearts and souls into making\x01",
            "these engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "I know I suck at expressing\x01",
            "my feelings, but...I don't want\x01",
            "anything to cheapen that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1BD4")

    TalkEnd(0xB)
    Return()

    # Function_7_19F0 end

    def Function_8_1BD8(): pass

    label("Function_8_1BD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C16")

    ChrTalk(    #77
        0xFE,
        (
            "Man, work just keeps piling\x01",
            "on up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C16")

    Jump("loc_1DCC")

    label("loc_1C19")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1C2F")
    Jump("loc_1DCC")

    label("loc_1C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_1C96")

    ChrTalk(    #78
        0xFE,
        "A new engine, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Judging by the look of it,\x01",
            "we can expect some real\x01",
            "high output.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCC")

    label("loc_1C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1CF0")

    ChrTalk(    #80
        0xFE,
        (
            "Phelio got a boxed lunch\x01",
            "from his loving wife...\x01",
            "*sigh* I really envy him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCC")

    label("loc_1CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D23")

    ChrTalk(    #81
        0xFE,
        (
            "Phew!\x01",
            "Worked my butt off today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCC")

    label("loc_1D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1D86")

    ChrTalk(    #82
        0xFE,
        (
            "Our receptionist's a newbie,\x01",
            "but he's been busting his butt\x01",
            "as much as us veterans.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCC")

    label("loc_1D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1DCC")

    ChrTalk(    #83
        0xFE,
        (
            "If you've got some work\x01",
            "to ask about, ask at the\x01",
            "counter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCC")

    TalkEnd(0xFE)
    Return()

    # Function_8_1BD8 end

    def Function_9_1DD0(): pass

    label("Function_9_1DD0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x05The new model engine for the Arseille is here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_1DD0 end

    SaveToFile()

Try(main)
