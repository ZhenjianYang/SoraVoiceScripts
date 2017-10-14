from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2700   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2700.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Private Nix',                          # 9
        'Private Vernon',                       # 10
        'Private Cromwell',                     # 11
        'Melvin',                               # 12
        'Aurian Causeway',                      # 13
        'Kaldia Tunnel',                        # 14
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH01760 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH01760P._CP',             # 03
    )

    DeclNpc(
        X                   = 18400,
        Z                   = 5000,
        Y                   = 1400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -18600,
        Z                   = 0,
        Y                   = 2300,
        Direction           = 270,
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
        X                   = 18400,
        Z                   = 5000,
        Y                   = 1400,
        Direction           = 270,
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
        X                   = -22780,
        Z                   = 0,
        Y                   = 6880,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -62340,
        Z                   = 0,
        Y                   = -1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 21320,
        Z                   = 5000,
        Y                   = 460,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 19830,
        TriggerZ            = 5000,
        TriggerY            = -50,
        TriggerRange        = 800,
        ActorX              = 19830,
        ActorZ              = 6000,
        ActorY              = -50,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -45890,
        TriggerZ            = 0,
        TriggerY            = 2240,
        TriggerRange        = 1500,
        ActorX              = -45890,
        ActorZ              = 1700,
        ActorY              = 2240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3110,
        TriggerZ            = 5000,
        TriggerY            = 2490,
        TriggerRange        = 1000,
        ActorX              = 7850,
        ActorZ              = -5000,
        ActorY              = 9160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_255",          # 01, 1
        "Function_2_2DD",          # 02, 2
        "Function_3_3AB",          # 03, 3
        "Function_4_48C",          # 04, 4
        "Function_5_A74",          # 05, 5
        "Function_6_152E",         # 06, 6
        "Function_7_1714",         # 07, 7
        "Function_8_1C55",         # 08, 8
        "Function_9_2933",         # 09, 9
        "Function_10_29CB",        # 0A, 10
        "Function_11_2A22",        # 0B, 11
        "Function_12_2A93",        # 0C, 12
        "Function_13_2A9F",        # 0D, 13
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_21E")
    SetChrPos(0x8, 18400, 5000, 1400, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B")
    ClearChrFlags(0xB, 0x80)

    label("loc_21B")

    Jump("loc_234")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_234")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_234")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_240"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_251")

    Jump("loc_254")

    label("loc_254")

    Return()

    # Function_0_1F6 end

    def Function_1_255(): pass

    label("Function_1_255")

    OP_16(0x2, 0xFA0, 0xFFFDC5B0, 0xFFFE0C00, 0x23004F)
    OP_E8(0xDC, 0x5, 0x0, 0x0)
    OP_1C(0x1, 0x0, 0xC)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_289"),
        (101, "loc_289"),
        (102, "loc_291"),
        (103, "loc_291"),
        (SWITCH_DEFAULT, "loc_299"),
    )


    label("loc_289")

    OP_22(0x1CE, 0x1, 0x64)
    Jump("loc_299")

    label("loc_291")

    OP_22(0x1CA, 0x1, 0x64)
    Jump("loc_299")

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD")
    OP_72(0x2, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_2C4")

    label("loc_2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2C4")
    OP_72(0x2, 0x10)
    OP_6F(0x2, 160)
    OP_64(0x0, 0x1)

    label("loc_2C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC")
    OP_72(0x1, 0x10)
    OP_6F(0x1, 99)

    label("loc_2DC")

    Return()

    # Function_1_255 end

    def Function_2_2DD(): pass

    label("Function_2_2DD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_395")

    label("loc_302")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_395")

    label("loc_31B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_334")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_395")

    label("loc_334")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_395")

    label("loc_34D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_395")

    label("loc_366")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_395")

    label("loc_37F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_395")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_395")

    label("loc_3AA")

    Return()

    # Function_2_2DD end

    def Function_3_3AB(): pass

    label("Function_3_3AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_412")

    ChrTalk(    #0
        0xFE,
        "I'm on watch today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "...Which makes me wonder who's\x01",
            "handling customs downstairs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_488")

    label("loc_412")

    OP_A2(0x2)

    ChrTalk(    #2
        0xFE,
        "Nix is off duty, so I'm on watch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "*sigh* Can't say I get why, but it's\x01",
            "all part of the job, so whatever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_488")

    TalkEnd(0xFE)
    Return()

    # Function_3_3AB end

    def Function_4_48C(): pass

    label("Function_4_48C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_5D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54C")

    ChrTalk(    #4
        0xFE,
        (
            "I can aim my gun, but it's not like\x01",
            "I can actually fire it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Just thinking about it has me\x01",
            "sweatin' a few bullets of my own,\x01",
            "so I'm trying not to dwell on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_5D0")

    label("loc_54C")


    ChrTalk(    #6
        0xFE,
        (
            "I can aim my gun, but it's not like\x01",
            "I can actually fire it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "We haven't done our bayonet\x01",
            "exercises in a long time, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D0")

    Jump("loc_A70")

    label("loc_5D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F0")

    ChrTalk(    #8
        0xFE,
        (
            "Guild bracers occasionally come\x01",
            "through here while on patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Unlike us, they're tasked with\x01",
            "keeping watch over entire regions.\x01",
            "Can't even imagine how tough that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "We can handle local patrol,\x01",
            "but patrolling like that's on a\x01",
            "whole different scale.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_796")

    label("loc_6F0")


    ChrTalk(    #11
        0xFE,
        (
            "Given the situation, though, even our\x01",
            "small-scale patrols are a necessity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Besides, seeing their level of\x01",
            "dedication makes me want to\x01",
            "step up my game, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_796")

    Jump("loc_A70")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_8DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_839")

    ChrTalk(    #13
        0xFE,
        (
            "Lately, there've been way more\x01",
            "dangerous monsters than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "That's our problem, though.\x01",
            "You guys should relax and take\x01",
            "a load off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DB")

    label("loc_839")

    OP_A2(0x1)

    ChrTalk(    #15
        0xFE,
        "Working hard as ever, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "You guys came a heck of a long way to\x01",
            "end up out here. You taking a detour while\x01",
            "hunting a wanted monster or something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DB")

    Jump("loc_A70")

    label("loc_8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_967")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_915")

    ChrTalk(    #17
        0xFE,
        "Apparently, Nix DID see a ghost.\x02",
    )

    CloseMessageWindow()
    Jump("loc_964")

    label("loc_915")

    OP_A2(0x1)

    ChrTalk(    #18
        0xFE,
        "Apparently, Nix DID see a ghost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "I'm sure glad I didn't see it...\x02",
    )

    CloseMessageWindow()

    label("loc_964")

    Jump("loc_A70")

    label("loc_967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9E9")

    ChrTalk(    #20
        0xFE,
        (
            "Not many tourists are coming through\x01",
            "these days. It's so boring, it's been a\x01",
            "struggle to keep my eyes open.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A70")

    label("loc_9E9")

    OP_A2(0x1)

    ChrTalk(    #21
        0xFE,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Not many tourists are coming through\x01",
            "these days. It's so boring, it's been a\x01",
            "struggle to keep my eyes open.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A70")

    TalkEnd(0xFE)
    Return()

    # Function_4_48C end

    def Function_5_A74(): pass

    label("Function_5_A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_C24")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB9")

    ChrTalk(    #23
        0xFE,
        (
            "I can still hardly believe some guy\x01",
            "braved the tunnel the way it is now\x01",
            "without batting an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I'd heard he was heading back to\x01",
            "Zeiss on urgent business, but could\x01",
            "anything be that urgent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "The guy's got balls, that's for sure.\x01",
            "Courage like that's almost enough to\x01",
            "steal a guy's heart.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_C1E")

    label("loc_BB9")


    ChrTalk(    #26
        0xFE,
        (
            "I can still hardly believe some guy\x01",
            "braved the tunnel the way it is now\x01",
            "without batting an eye.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1E")

    TalkEnd(0xFE)
    Jump("loc_152D")

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D01")
    TalkBegin(0xFE)

    ChrTalk(    #27
        0xFE,
        (
            "It's pitch black in there right now!\x01",
            "I'd be terrified. Brrrr...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Think about it! A monster could leap at you\x01",
            "at any moment, and you'd be none the wiser.\x01",
            "I'd be freaking out every step of the way.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_152D")

    label("loc_D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_END)), "loc_143D")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DC5")

    ChrTalk(    #29
        0xFE,
        (
            "The signing ceremony is close,\x01",
            "so we're buckling down on security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I know it's a big deal--really, I do--\x01",
            "but what could possibly happen all\x01",
            "the way out here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_DC5")


    ChrTalk(    #31
        0xFE,
        (
            "The signing ceremony is close,\x01",
            "so we're buckling down on security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "It'd make sense if we were around the\x01",
            "capital, but we're nowhere near there.\x01",
            "There's no point, if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E83")

    Jump("loc_1437")

    label("loc_E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F3F")

    ChrTalk(    #33
        0xFE,
        (
            "Those two bracers I saw looked like\x01",
            "they were in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Phew! Man, I feel sorry for anyone\x01",
            "in that line of work. Poor guys barely\x01",
            "have a second to breathe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBF")

    label("loc_F3F")


    ChrTalk(    #35
        0xFE,
        (
            "Two bracers passed by here\x01",
            "a short while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "You didn't happen to see\x01",
            "them while going through\x01",
            "yourself, did you?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_FBF")

    Jump("loc_1437")

    label("loc_FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(    #37
        0xFE,
        (
            "The area around the Kaldia Hills\x01",
            "have a very stable base.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "That's why there are almost\x01",
            "no earthquakes on record.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1110")

    label("loc_104D")


    ChrTalk(    #39
        0xFE,
        (
            "We've received several reports\x01",
            "of earthquakes around Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Earthquakes don't typically happen in\x01",
            "Liberl, so it's a little unsettling to hear\x01",
            "about multiple ones in a row like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1110")

    Jump("loc_1437")

    label("loc_1113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1193")

    ChrTalk(    #41
        0xFE,
        (
            "Well, not much we can do about it.\x01",
            "Since you guys are already here, why\x01",
            "not come in and rest for a while?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1216")

    label("loc_1193")


    ChrTalk(    #42
        0xFE,
        "Hey, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "If you're coming here through the tunnel,\x01",
            "you must either be insanely brave or on\x01",
            "a hell of an urgent job.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1216")

    Jump("loc_1437")

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12C7")

    ChrTalk(    #44
        0xFE,
        (
            "I've been on pins and needles every\x01",
            "night since I saw that thing. What if\x01",
            "it shows up again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Please, pleeease, solve this case\x01",
            "as soon as you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1361")

    label("loc_12C7")

    OP_A2(0x0)

    ChrTalk(    #46
        0xFE,
        "Heya. How's the investigation going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I won't lie, I'm still pretty freaked\x01",
            "out. If you guys don't solve this soon,\x01",
            "I might see...IT...again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1361")

    Jump("loc_1437")

    label("loc_1364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 2)), scpexpr(EXPR_END)), "loc_1437")

    ChrTalk(    #48
        0xFE,
        (
            "It's nice to know I wasn't just seein'\x01",
            "things, but fat load of good it does me\x01",
            "now. Everyone's already pissed off at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "*sigh* My life's gone from bad to worse\x01",
            "ever since that thing showed up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1437")

    TalkEnd(0x8)
    Jump("loc_152D")

    label("loc_143D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 2)), scpexpr(EXPR_END)), "loc_144B")
    Call(0, 8)
    Jump("loc_152D")

    label("loc_144B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14A7")

    ChrTalk(    #50
        0xFE,
        (
            "The tunnel is as dark as it is long,\x01",
            "so not many go through here, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152A")

    label("loc_14A7")

    OP_A2(0x0)

    ChrTalk(    #51
        0xFE,
        "This is the entrance to the Kaldia Tunnel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "If you don't have permission to pass,\x01",
            "I'm afraid you can't go any farther.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152A")

    TalkEnd(0x8)

    label("loc_152D")

    Return()

    # Function_5_A74 end

    def Function_6_152E(): pass

    label("Function_6_152E")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165E")

    ChrTalk(    #53
        0xFE,
        "What's up? Working hard, I hope!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I'm Melvin, by the way. I'm a junior\x01",
            "bracer with the Ruan branch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I'm currently tasked with doing the\x01",
            "rounds and patrolling aaaaall over\x01",
            "the region!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "It's kind of a pain, but it's perfect\x01",
            "for a guy with tons of stamina like\x01",
            "me!! Whoo!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1710")

    label("loc_165E")


    ChrTalk(    #57
        0xFE,
        (
            "I'm currently tasked with doing the\x01",
            "rounds and patrolling aaaaall over\x01",
            "the region!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "It's kind of a pain, but it's perfect\x01",
            "for a guy with tons of stamina like\x01",
            "me!! Whoo!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1710")

    TalkEnd(0xB)
    Return()

    # Function_6_152E end

    def Function_7_1714(): pass

    label("Function_7_1714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1725")
    Call(0, 9)

    label("loc_1725")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_4A(0x8, 255)
    OP_6D(5900, 12000, 13400, 0)
    OP_6C(85000, 0)
    OP_6B(8000, 0)
    StopSound(0x7D00, 0x3D090, 0x0)
    SetChrPos(0x101, -52500, 0, -1800, 90)
    SetChrPos(0xF7, -52500, 0, -600, 90)
    OP_C8(0x200, 0x46, "C_PLAC05._CH", 0x0, 0x7D0)
    OP_DE("Air-Letten")
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x1FBD0, 0x2EE0)

    def lambda_17BF():
        OP_6B(2800, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17BF)

    def lambda_17CF():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17CF)
    Sleep(3000)

    def lambda_17E4():
        OP_6D(-50000, 0, -1500, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17E4)
    Sleep(8500)

    ChrTalk(    #59
        0x101,
        (
            "#1011F#2PAir-Letten Checkpoint...\x01",
            "Feels like ages since I've been here.\x02\x03",

            "#1016FSo the guard who saw...IT...\x01",
            "is around here somewhere...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1A4A")

    ChrTalk(    #60
        0x106,
        (
            "#051F#5PLeast that's what Jean told us, yeah.\x02\x03",

            "Let's hit up the guard commander here\x01",
            "first and see who saw what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1015F#2PGood idea.\x02\x03",

            "#1007FBut... *sigh*...\x02\x03",

            "To think someone saw IT in\x01",
            "such a lovely place...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)
    Sleep(500)

    ChrTalk(    #62
        0x106,
        (
            "#552F#5POh, knock it off with the 'IT' nonsense.\x02\x03",

            "Just say it's a ghost or whatever already.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #63
        0x101,
        (
            "#1014F#2PNo, NO! Not hearing anything!\x01",
            "LA LA LA!\x02\x03",

            "Can't a girl lie to herself\x01",
            "every now and then?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4B")

    label("loc_1A4A")


    ChrTalk(    #64
        0x103,
        (
            "#020F#5PAccording to Jean's information, yes.\x02\x03",

            "First, we should speak with the guard\x01",
            "commander here about who saw our phantom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1015F#2PGood idea.\x02\x03",

            "#1007FBut... *sigh*...\x02\x03",

            "To think someone saw IT in\x01",
            "such a lovely place...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #66
        0x103,
        (
            "#027F#5PEstelle...it's not good to lie\x01",
            "to yourself, you know.\x02\x03",

            "Why not stop referring to our ghost\x01",
            "as 'IT' and simply call it what it is?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #67
        0x101,
        (
            "#1014F#2PNot listening! Noooooooot listening!\x02\x03",

            "I don't have to admit that IT exists!\x01",
            "Nooooooot liiiiiiistening...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4B")

    OP_A2(0x1211)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_7_1714 end

    def Function_8_1C55(): pass

    label("Function_8_1C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C6F")
    Call(0, 9)
    FadeToBright(0, 0)

    label("loc_1C6F")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_4A(0x8, 255)
    Fade(1000)
    SetChrPos(0x101, 16230, 5000, 1730, 90)
    SetChrPos(0xF7, 16120, 5000, 530, 45)
    OP_6B(2800, 0)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(    #68
        0x8,
        (
            "Ho, there! You want to head\x01",
            "into the tunnel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "Give me just a minute and\x01",
            "I'll open the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1016FAh, no. We're not here for the tunnel.\x02\x03",

            "#1000FWe're from the Bracer Guild.\x02\x03",

            "And we're here for you, actually!\x01",
            "Can we ask you about the 'white\x01",
            "shadow' you saw?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x8,
        "Hang on, you mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "B-But that was just something I dreamed\x01",
            "up when I was half-asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1002FActually, it wasn't.\x02\x03",

            "A lot of people across Ruan\x01",
            "have been seeing...it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F72")

    ChrTalk(    #74
        0x106,
        (
            "#051F#2PAnd, according to your commanding\x01",
            "officer, neither you nor he knew.\x02\x03",

            "He said 'sorry' for his earlier comments,\x01",
            "and says you can talk freely 'bout it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2031")

    label("loc_1F72")


    ChrTalk(    #75
        0x103,
        (
            "#020F#2PAnd, according to your commanding\x01",
            "officer, neither you nor he knew.\x02\x03",

            "He apologized for his earlier comments,\x01",
            "and told us to let you know you can\x01",
            "speak freely about what you saw.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2031")


    ChrTalk(    #76
        0x8,
        "So it WAS real!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "I knew it was too real to be a dream!\x01",
            "This makes me feel a bit better, honestly.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x8,
        (
            "...Though if that thing was real,\x01",
            "it's actually kinda bone-chilling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1007FTrust me, I know what you mean.\x02\x03",

            "#1008FA-Anyway, can you tell us\x01",
            "about what you saw?\x02\x03",

            "In as much detail as you can,\x01",
            "please!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        "Sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "It was three nights ago. I was\x01",
            "standing here on my watch shift...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "You've noticed how loud the\x01",
            "waterfall is, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "You get used to it after a while,\x01",
            "and it has a rhythm that can\x01",
            "really lull you to sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "Plus, I'd just started my shift and had come\x01",
            "from the mess, so I was even more sleepy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "So to keep from falling asleep,\x01",
            "I walked back and forth around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        "And that's when I saw...IT.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1002FI-I see.\x02\x03",

            "What...was it, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "A floating man dressed in white,\x01",
            "old-fashioned clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "He...or it...was dancing just\x01",
            "above the waterfall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "I freaked out so bad, I pointed my\x01",
            "rifle at it without thinking, and...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #91
        0x101,
        (
            "#1004FWha?!\x02\x03",

            "You SHOT the gh--the thing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "Yeah. I meant it to be a warning shot, but...\x01",
            "I was so nervous I hit it right in the chest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "Or, I KNOW I did, but...it just floated\x01",
            "there as if nothing had happened at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "After that, it took off like a bird\x01",
            "or something, heading north.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1013FEeeep...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_25C7")

    ChrTalk(    #96
        0x106,
        (
            "#552F#2PImmune to gunfire, too.\x01",
            "That's just swell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_261B")

    label("loc_25C7")


    ChrTalk(    #97
        0x103,
        (
            "#025F#2POh, my... It can't be affected by gunfire?\x01",
            "That'd suggest...something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_261B")


    ChrTalk(    #98
        0x8,
        (
            "After all that, I ran inside and\x01",
            "woke the commander, of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "But all that got me was a dressing-\x01",
            "down for 'sleeping on the job' and\x01",
            "'unnecessary rifle discharge'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        "Man...that was a bad day.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #101
        0x101,
        (
            "#1025FI can, um, imagine...\x02\x03",

            "#1016FWell, anyway, it's clearly for the\x01",
            "best to just pretend it was a dream\x01",
            "and forget it ever happened! Yep!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "Thanks for the thought, but I doubt\x01",
            "I'll ever be able to forget that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "I dunno why that poor soul is a wandering\x01",
            "ghost, but try to help him, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "I mean, bracers can solve the\x01",
            "problems of the dead too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1007FH-Heck no! I'm no priest!\x02\x03",

            "#1015FBut...there has to be a reason\x01",
            "it's showing up, yeah.\x02\x03",

            "We need to figure out what\x01",
            "that reason is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        "Good luck, then!\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_A2(0x1213)
    OP_28(0x82, 0x2, 0x4)
    OP_28(0x82, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_8_1C55 end

    def Function_9_2933(): pass

    label("Function_9_2933")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29AC"),
        (1, "loc_29B2"),
        (SWITCH_DEFAULT, "loc_29B8"),
    )


    label("loc_29AC")

    OP_A2(0x1200)
    Jump("loc_29B8")

    label("loc_29B2")

    OP_A2(0x1201)
    Jump("loc_29B8")

    label("loc_29B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_29C6")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_29CA")

    label("loc_29C6")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_29CA")

    Return()

    # Function_9_2933 end

    def Function_10_29CB(): pass

    label("Function_10_29CB")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #107
        "\x07\x05The door is tightly closed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_29CB end

    def Function_11_2A22(): pass

    label("Function_11_2A22")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #108
        (
            "\x07\x05West: City of Ruan - 175 selge\x01",
            "East: City of Zeiss - 448 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_2A22 end

    def Function_12_2A93(): pass

    label("Function_12_2A93")

    TalkBegin(0xFF)
    Sleep(200)
    TalkEnd(0xFF)
    Return()

    # Function_12_2A93 end

    def Function_13_2A9F(): pass

    label("Function_13_2A9F")

    EventBegin(0x1)

    ChrTalk(    #109
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_2ACB():
        OP_6D(3950, 5000, 6930, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2ACB)

    def lambda_2AE3():
        OP_6B(3250, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2AE3)

    def lambda_2AF3():
        OP_6C(60000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2AF3)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #110
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C66")
    OP_C0(0xE, 0x1A, 0xCE4, 0x1838, 0xD3E, 0x0, 0xC8A, 0xFFFFFC18, 0x1A72)
    Fade(500)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    SetChrChipByIndex(0x0, 65535)
    ClearChrFlags(0x0, 0x2)
    ClearChrFlags(0x0, 0x40)
    ClearChrFlags(0x0, 0x4)
    SetChrPos(0x0, 4210, 5000, 2040, 0)
    SetChrPos(0x1, 4210, 5000, 2040, 0)
    SetChrPos(0x2, 4210, 5000, 2040, 0)
    SetChrPos(0x3, 4210, 5000, 2040, 0)
    SetChrPos(0x4, 4210, 5000, 2040, 0)
    SetChrPos(0x5, 4210, 5000, 2040, 0)
    SetChrPos(0x6, 4210, 5000, 2040, 0)
    SetChrPos(0x7, 4210, 5000, 2040, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_2C75")

    label("loc_2C66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C75")
    EventEnd(0x1)

    label("loc_2C75")

    Return()

    # Function_13_2A9F end

    SaveToFile()

Try(main)
