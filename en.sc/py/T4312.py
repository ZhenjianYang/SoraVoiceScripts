from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4312   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4312.x',
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
        'Chamberlain Raymond',                  # 9
        'Lt. Colonel Cid',                      # 10
        'Warrant Officer Belc',                 # 11
        'Simone',                               # 12
        'Royal Army Soldier',                   # 13
        'Nena',                                 # 14
        'Royal Army Soldier',                   # 15
        'Royal Army Soldier',                   # 16
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
        'ED6_DT07/CH01570 ._CH',             # 00
        'ED6_DT27/CH03590 ._CH',             # 01
        'ED6_DT07/CH01600 ._CH',             # 02
        'ED6_DT07/CH01350 ._CH',             # 03
        'ED6_DT07/CH01640 ._CH',             # 04
        'ED6_DT07/CH01770 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01570P._CP',             # 00
        'ED6_DT27/CH03590P._CP',             # 01
        'ED6_DT07/CH01600P._CP',             # 02
        'ED6_DT07/CH01350P._CP',             # 03
        'ED6_DT07/CH01640P._CP',             # 04
        'ED6_DT07/CH01770P._CP',             # 05
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
        Direction           = 0,
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
        X                   = -9300,
        Z                   = 0,
        Y                   = 400,
        Direction           = 0,
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
        X                   = 15260,
        Z                   = 0,
        Y                   = -1160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 7340,
        Z                   = 0,
        Y                   = 58660,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -49260,
        Z                   = 0,
        Y                   = 20160,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -53120,
        Z                   = 0,
        Y                   = 20160,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 250,
        TriggerY            = 70040,
        TriggerRange        = 500,
        ActorX              = 0,
        ActorZ              = 1250,
        ActorY              = 70040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_30D",          # 01, 1
        "Function_2_319",          # 02, 2
        "Function_3_496",          # 03, 3
        "Function_4_543",          # 04, 4
        "Function_5_EDA",          # 05, 5
        "Function_6_102C",         # 06, 6
        "Function_7_1378",         # 07, 7
        "Function_8_15CE",         # 08, 8
        "Function_9_16D5",         # 09, 9
        "Function_10_188F",        # 0A, 10
        "Function_11_1E29",        # 0B, 11
        "Function_12_3082",        # 0C, 12
        "Function_13_30B5",        # 0D, 13
        "Function_14_30FD",        # 0E, 14
        "Function_15_3145",        # 0F, 15
        "Function_16_318D",        # 10, 16
        "Function_17_31D5",        # 11, 17
        "Function_18_346A",        # 12, 18
        "Function_19_44CD",        # 13, 19
        "Function_20_4565",        # 14, 20
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_216")
    ClearChrFlags(0xC, 0x80)

    label("loc_216")

    Jump("loc_2D2")

    label("loc_219")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_254")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 900, 0, 66800, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_2D2")

    label("loc_254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_299")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 900, 0, 66800, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -840, 0, 66800, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_2D2")

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_2D2")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_END)), "loc_2C6")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2D2")

    label("loc_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 4)), scpexpr(EXPR_END)), "loc_2D2")
    ClearChrFlags(0xD, 0x80)

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E8")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_30C")

    label("loc_2E8")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2F4"),
        (SWITCH_DEFAULT, "loc_30C"),
    )


    label("loc_2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_309")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_309")

    Jump("loc_30C")

    label("loc_30C")

    Return()

    # Function_0_1FE end

    def Function_1_30D(): pass

    label("Function_1_30D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_318")
    OP_64(0x0, 0x1)

    label("loc_318")

    Return()

    # Function_1_30D end

    def Function_2_319(): pass

    label("Function_2_319")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_480")

    label("loc_33E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_357")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_480")

    label("loc_357")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_370")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_480")

    label("loc_370")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_389")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_480")

    label("loc_389")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_480")

    label("loc_3A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_480")

    label("loc_3BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D4")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_480")

    label("loc_3D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_480")

    label("loc_3ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_406")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_480")

    label("loc_406")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_480")

    label("loc_41F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_438")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_480")

    label("loc_438")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_480")

    label("loc_451")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_480")

    label("loc_46A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_480")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_495")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_480")

    label("loc_495")

    Return()

    # Function_2_319 end

    def Function_3_496(): pass

    label("Function_3_496")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_542")
    OP_8E(0xFE, 0x3B9C, 0x0, 0xFFFFFB78, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC464, 0x0, 0xFFFFFB78, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFBEEC, 0x0, 0xFFFFF664, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFBEEC, 0x0, 0xFFFFF0EC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC464, 0x0, 0xFFFFEC14, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3B9C, 0x0, 0xFFFFEC14, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4114, 0x0, 0xFFFFF0EC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4114, 0x0, 0xFFFFF664, 0x7D0, 0x0)
    Jump("Function_3_496")

    label("loc_542")

    Return()

    # Function_3_496 end

    def Function_4_543(): pass

    label("Function_4_543")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_95B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 7)), scpexpr(EXPR_END)), "loc_5DA")

    ChrTalk(    #0
        0x9,
        (
            "#701FWe will see security for the\x01",
            "signing ceremony dealt with.\x02\x03",

            "If you're heading to the Bose region,\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958")

    label("loc_5DA")


    ChrTalk(    #1
        0x9,
        (
            "#701FHello there, everyone.\x02\x03",

            "Your assistance was much appreciated on\x01",
            "this case.\x02\x03",

            "Allow me to offer my thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000FNo, no... I don't know what we would have\x01",
            "done if Julia hadn't come.\x02\x03",

            "You called Julia, right, Colonel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#701FHaha, yes, well...\x02\x03",

            "#703FHowever, I think it all worked precisely\x01",
            "because of your assistance.\x02\x03",

            "#701FI hope the army can continue to\x01",
            "rely on the guild's assistance.\x02\x03",

            "Especially against the society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1000FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#701FWill you be departing the capital after this,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1000FYeah, next we're heading to the Bose region\x01",
            "where the Special Ops guys appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#703FI thought so...\x02\x03",

            "#700FApparently General Morgan has begun\x01",
            "a large scale investigation in Bose.\x02\x03",

            "Be careful over there, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1000FThanks. Good luck with the security of the\x01",
            "signing ceremony on your end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "#701FYes, thank you. I promise I'll see it through.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x165F)

    label("loc_958")

    Jump("loc_ED6")

    label("loc_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_DEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 0)), scpexpr(EXPR_END)), "loc_A30")

    ChrTalk(    #10
        0x9,
        (
            "#703FStill, to think the Intelligence Division\x01",
            "was hiding in the Bose region.\x02\x03",

            "#700FI guess I should expect that they'd be able to\x01",
            "escape General Morgan's investigation and\x01",
            "stay in hiding...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE9")

    label("loc_A30")


    ChrTalk(    #11
        0x9,
        (
            "#703FStill, to think the Intelligence Division\x01",
            "was hiding in the Bose region.\x02\x03",

            "#700FI guess I should expect that they'd be able to\x01",
            "escape General Morgan's investigation and\x01",
            "stay in hiding...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12F,
        (
            "#264FIs this mister 'Intelligence Divisiony' good\x01",
            "at hiding?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x12F, 400)

    ChrTalk(    #13
        0x9,
        (
            "#701FWell, they are a force specially trained to be able\x01",
            "to perform information gathering in any and all\x01",
            "circumstances, after all.\x02\x03",

            "#700FThey're especially skilled at survival techniques\x01",
            "like infiltrating and staying hidden in enemy\x01",
            "territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x12F,
        (
            "#265FOkay, I want to play hide and seek\x01",
            "with the Special Ops people!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        "#702FH-Hide and seek?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12F, 400)

    ChrTalk(    #16
        0x101,
        "#1016FThaaaaat's not gonna happen.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #17
        0x12F,
        (
            "#264FOh, why's that?\x02\x03",

            "#263FRenne is pretty confident she wouldn't\x01",
            "lose at hide and seek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1015FWell, you might win, sure, Renne.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#701FHaha. Sorry, young miss, but I don't think\x01",
            "they're the kind of people that would play\x01",
            "with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x12F,
        "#267FReally? How boring...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1660)

    label("loc_DE9")

    Jump("loc_ED6")

    label("loc_DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_ED6")

    ChrTalk(    #21
        0x9,
        (
            "#700FThe fugitive Intelligence Division now reveal\x01",
            "themselves...\x02\x03",

            "The problem is determining whether or not this\x01",
            "case is related to the signing ceremony...\x02\x03",

            "#703FOne way or another, I need more\x01",
            "information than just this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED6")

    TalkEnd(0x9)
    Return()

    # Function_4_543 end

    def Function_5_EDA(): pass

    label("Function_5_EDA")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_FB9")

    ChrTalk(    #22
        0xFE,
        (
            "It seems like it was a pair of bracers that\x01",
            "tracked down the Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "There might be some new information\x01",
            "at the capital guild branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "You should hurry back to Grancel.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1028")

    label("loc_FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1028")

    ChrTalk(    #25
        0xFE,
        (
            "Even if the site was Bose, there might\x01",
            "be requests for reinforcements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "We need to be alert...\x02",
    )

    CloseMessageWindow()

    label("loc_1028")

    TalkEnd(0xA)
    Return()

    # Function_5_EDA end

    def Function_6_102C(): pass

    label("Function_6_102C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_124B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 6)), scpexpr(EXPR_END)), "loc_107B")

    ChrTalk(    #27
        0xFE,
        "Everyone...please take care of that girl.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1248")

    label("loc_107B")

    TurnDirection(0xFE, 0x12F, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)

    ChrTalk(    #28
        0xFE,
        "Oh, that girl is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "There you ARE!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12F,
        (
            "#261FHeehee, it was fun playing hide and seek\x01",
            "with you, miss maid.\x02\x03",

            "#260FI'm gonna go back to the guild.\x02\x03",

            "I'm gonna wait for my papa and mama\x01",
            "to pick me up there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Uh... Oh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "...If you ever want to play hide and seek\x01",
            "again, come by again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I'll ask Raymond and spend as much\x01",
            "time with you as you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12F,
        "#261FReally? Thank you, miss.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x165E)

    label("loc_1248")

    Jump("loc_1374")

    label("loc_124B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_END)), "loc_1374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12CD")

    ChrTalk(    #36
        0xFE,
        "Really, that girl, making fools of grown-ups...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Once I catch her she's getting a hundred\x01",
            "spanks! Hmph!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1374")

    label("loc_12CD")


    ChrTalk(    #38
        0xFE,
        (
            "Hmm... Seems like she's not hiding around\x01",
            "here, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "Really, that girl, making fools of grown-ups...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "I wonder if Raymond hasn't already found her...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1374")

    TalkEnd(0xB)
    Return()

    # Function_6_102C end

    def Function_7_1378(): pass

    label("Function_7_1378")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13FE")

    ChrTalk(    #41
        0xFE,
        (
            "It's pretty worrisome to not have\x01",
            "much information come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "I hope orbments start working again soon.\x02",
    )

    CloseMessageWindow()

    label("loc_13FE")

    Jump("loc_15CA")

    label("loc_1401")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_14F0")

    ChrTalk(    #43
        0xFE,
        (
            "Apparently the sky bandits appeared\x01",
            "in Bose on the day of the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Those sky bandits... Weren't they the ones who\x01",
            "got pretty far in the Martial Arts Competition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "I hope nothing too bad happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_15CA")

    label("loc_14F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_15CA")

    ChrTalk(    #46
        0xFE,
        (
            "This morning an extermination of all monsters\x01",
            "on the Erbe Scenic Route was held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Well, it was basically like a practice session\x01",
            "before security really gets serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "Perfect for a warm-up, really.\x02",
    )

    CloseMessageWindow()

    label("loc_15CA")

    TalkEnd(0xC)
    Return()

    # Function_7_1378 end

    def Function_8_15CE(): pass

    label("Function_8_15CE")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_165B")

    ChrTalk(    #49
        0xFE,
        (
            "If you're looking for Colonel Cid,\x01",
            "he's in this room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "If you wish to meet with him, please,\x01",
            "pass through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D1")

    label("loc_165B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_16BA")

    ChrTalk(    #51
        0xFE,
        (
            "Apparently we're going to be on level 2 alert\x01",
            "status! I wonder what happened...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D1")

    label("loc_16BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_16D1")

    ChrTalk(    #52
        0xFE,
        "Good work!\x02",
    )

    CloseMessageWindow()

    label("loc_16D1")

    TalkEnd(0xE)
    Return()

    # Function_8_15CE end

    def Function_9_16D5(): pass

    label("Function_9_16D5")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1778")

    ChrTalk(    #53
        0xFE,
        (
            "Hey, seems like you caught the Special Ops\x01",
            "troops in cooperation with the Royal Guard,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "Got some business with Colonel Cid?\x02",
    )

    CloseMessageWindow()
    Jump("loc_188B")

    label("loc_1778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_182B")

    ChrTalk(    #55
        0xFE,
        "Level 2 alert status...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Does that mean someone's gonna try to\x01",
            "sabotage the signing ceremony?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I think I heard something about\x01",
            "the Intelligence Division...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188B")

    label("loc_182B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_188B")

    ChrTalk(    #58
        0xFE,
        (
            "The commander ran out of the room looking\x01",
            "very pale...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "I wonder what happened.\x02",
    )

    CloseMessageWindow()

    label("loc_188B")

    TalkEnd(0xF)
    Return()

    # Function_9_16D5 end

    def Function_10_188F(): pass

    label("Function_10_188F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1906")

    ChrTalk(    #60
        0xFE,
        "...Still not shiny enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I need to really put my back into\x01",
            "polishing this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197D")

    label("loc_1906")


    ChrTalk(    #62
        0xFE,
        "La la la la... ♪ Lala la laaa... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Polish it to a shiiiiine... ♪\x01",
            "A wonderful, beautiful shiiiine... ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_197D")

    Jump("loc_1E25")

    label("loc_1980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 4)), scpexpr(EXPR_END)), "loc_1E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A39")

    ChrTalk(    #64
        0xFE,
        (
            "This is the Crest Room where the non-aggression\x01",
            "pact signing ceremony will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "So I just naturally end up putting a\x01",
            "lot of effort into my cleaning here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E25")

    label("loc_1A39")


    ChrTalk(    #66
        0xFE,
        (
            "This is the Crest Room where the non-aggression\x01",
            "pact signing ceremony will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1011FHuh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Yes, of course on the day itself there won't just\x01",
            "be ambassadors from the Empire and Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "There'll also be a representative\x01",
            "from our Liberl Kingdom present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1015FI didn't really get a chance to look at this\x01",
            "place when I was here during the coup d'etat.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CFF")

    ChrTalk(    #71
        0x105,
        (
            "#048FHeehee. It's kind of nostalgic.\x02\x03",

            "You saved me when I was held here.\x02\x03",

            "It's touching to know the room from that\x01",
            "time is being used for the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1001FHaha, yeah.\x02\x03",

            "#1006FStill, though, now that I can just relax and\x01",
            "have a good look at it, it really is a very\x01",
            "dignified room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D56")

    label("loc_1CFF")


    ChrTalk(    #73
        0x101,
        (
            "#1006FNow that I'm really looking at it, this\x01",
            "is a pretty dignified-looking room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D56")


    ChrTalk(    #74
        0xFE,
        "Absolutely!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "That's why I always work extra hard when\x01",
            "I clean it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1016FAhaha, I'm not great at cleaning,\x01",
            "but I understand how you feel.\x02\x03",

            "#1001FWell, good luck with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "Yes, thank you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1E25")

    TalkEnd(0xD)
    Return()

    # Function_10_188F end

    def Function_11_1E29(): pass

    label("Function_11_1E29")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E40")
    Call(0, 19)
    Call(0, 20)

    label("loc_1E40")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 0, 0, -1790, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    OP_69(0x8, 0x0)
    FadeToBright(2000, 0)
    OP_43(0x8, 0x1, 0x0, 0xC)
    OP_0D()

    ChrTalk(    #78
        0x8,
        "Oh, dear, oh, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "The bracers will be here any minute!\x01",
            "Where could she have gone...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 0, 0, -9300, 0)

    ChrTalk(    #80
        0x101,
        "#1PHellooooo!\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #81
        0x8,
        "Ah! Yes, yes, may I ask what you--\x02",
    )

    CloseMessageWindow()

    def lambda_1F83():
        OP_6D(630, 0, -3120, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F83)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x10)
    WaitChrThread(0xF7, 0x1)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2061")

    ChrTalk(    #82
        0x8,
        "#6POH! You, are you...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #83
        0x108,
        "#070FHey! Been a while!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1016FHaha! Hello!\x01",
            "I guess you remember us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20AF")

    label("loc_2061")


    ChrTalk(    #85
        0x8,
        "#6PHm? Wait, you're...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1016FHaha! Hello!\x01",
            "I guess you remember us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_228C")

    ChrTalk(    #87
        0x8,
        "#6PHah! How could I forget!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "#6PWe all owe you greatly for\x01",
            "what you did at the villa.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(    #89
        0x8,
        "#6PAnd, wait, that's--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x105,
        "#542FIs something...wrong, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        "#6PEr, no, haha... No, I'm mistaken.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        "#6PYou just look like someone I know, miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x105,
        (
            "#048FOh, do I remind you of your\x01",
            "girlfriend, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "#6PAaaah! Umm, not at all!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    Sleep(500)

    ChrTalk(    #95
        0x8,
        (
            "#6PEr, so, I take it you are the team\x01",
            "Elnan said would be coming?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_228C")


    ChrTalk(    #96
        0x8,
        "#6PHah! How could I forget!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "#6PWe all owe you greatly for\x01",
            "what you did at the villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#6PSo, I take it you are the team\x01",
            "Elnan said would be coming?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232E")


    ChrTalk(    #99
        0x101,
        (
            "#1011FYeah, that's right.\x02\x03",

            "Is everything okay, though?\x01",
            "You seem kinda...troubled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        "#6PIt's...about that lost child, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#6PShe's, um, how to put this...'lost again.'\x01",
            "She told me, 'Let's play hide and seek'\x01",
            "and just vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        "#6PI've been looking for her ever since!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1016FOh, um...crap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#6PI'll find her soon, I swear!\x01",
            "Please, wait in the lounge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        "#6PYou know where that is, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1015FWell, yeah, I do, but..\x02\x03",

            "You look like you're having some trouble.\x01",
            "You're sure you don't want a hand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "#6PAre you sure?\x01",
            "I wouldn't want to impose...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25FD")

    ChrTalk(    #108
        0x106,
        (
            "#051F#2PHey, we're already on the case, right?\x02\x03",

            "Tell us her name and what she looks\x01",
            "like and we'll get lookin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2696")

    label("loc_25FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2696")

    ChrTalk(    #109
        0x103,
        (
            "#021F#2PIt's a bit late for us to back\x01",
            "out now, anyway.\x02\x03",

            "#020FIf you could give us her name and\x01",
            "description, we'll look for the girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2696")


    ChrTalk(    #110
        0x8,
        "#6PThank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#6PShe's a pre-teen girl wearing a white,\x01",
            "frilly dress and a black hair ribbon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        "#6PShe never gave me her name, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1004FYou didn't find out her name?\x01",
            "Seriously?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "#6PShe wouldn't tell me! Every time I asked\x01",
            "she just said, 'It's a seeee-cret!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#6PI think she came in with her family,\x01",
            "but I couldn't find her parents or anyone\x01",
            "who knew her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#6PMy only option was to call you,\x01",
            "in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1016FI, uh, I see!\x02\x03",

            "#1000FHide and seek, huh?\x01",
            "Energetic little girl you got there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        "#6PHm. Not sure I'd say 'energetic.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        "#6PPrecocious and whimsical is more like it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        (
            "#6PI got the distinct impression she was\x01",
            "enjoying toying with the adults around\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_299D")

    ChrTalk(    #121
        0x104,
        "#035FOhoooo. A prank-loving kitten, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A44")

    label("loc_299D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0A")

    ChrTalk(    #122
        0x103,
        (
            "#027F#2PSo a prankster-kitten kind of girl.\x01",
            "Reminds me just a bit of someone I know...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A44")

    label("loc_2A0A")


    ChrTalk(    #123
        0x101,
        (
            "#1015FSo...sort of a prank-loving kind of\x01",
            "girl, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A44")


    ChrTalk(    #124
        0x8,
        "#6PYes, exactly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        "#6PAgh! Where could she have gotten off to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        (
            "#6PI'm fairly sure she hasn't left the\x01",
            "building, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B6B")

    ChrTalk(    #127
        0x104,
        (
            "#030FIn other words, we must search the\x01",
            "entire building, including the courtyard.\x02\x03",

            "#031FHeh! A perfect place for a game of\x01",
            "kitten-and-mouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BF9")

    ChrTalk(    #128
        0x108,
        (
            "#070FMeaning we need to check the entire\x01",
            "building, including the courtyard.\x02\x03",

            "Sounds about right for an energetic child.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2BF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CA8")

    ChrTalk(    #129
        0x105,
        (
            "#040FSo we should probably search the entire\x01",
            "building, including the courtyard.\x02\x03",

            "#041FHaha. The villa IS a great place to play\x01",
            "hide and seek with a kitten.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA8")


    ChrTalk(    #130
        0x8,
        "#6PI will wait in the lounge, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "#6PWhen you find her, please bring\x01",
            "her there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1006FWill do!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    def lambda_2D25():
        OP_6D(-1400, 0, -3120, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D25)

    def lambda_2D3D():

        label("loc_2D3D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D3D")

    QueueWorkItem2(0x101, 1, lambda_2D3D)

    def lambda_2D4E():

        label("loc_2D4E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D4E")

    QueueWorkItem2(0xF7, 1, lambda_2D4E)

    def lambda_2D5F():

        label("loc_2D5F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D5F")

    QueueWorkItem2(0xF8, 1, lambda_2D5F)

    def lambda_2D70():

        label("loc_2D70")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D70")

    QueueWorkItem2(0xF9, 1, lambda_2D70)
    OP_8E(0x8, 0xFFFFDCB0, 0x0, 0xFFFFFACE, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    def lambda_2DB4():
        OP_6D(-260, 0, -4800, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2DB4)

    def lambda_2DCC():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DCC)
    Sleep(50)

    def lambda_2DDF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2DDF)
    Sleep(50)

    def lambda_2DF2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2DF2)
    Sleep(50)

    def lambda_2E05():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2E05)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #133
        0x101,
        (
            "#1006FOkay, let's hunt us down a kitten...child!\x02\x03",

            "So, white dress, black hair ribbon.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ED2")

    ChrTalk(    #134
        0x107,
        (
            "#061FHeehee! That shouldn't be too hard\x01",
            "to find!\x02\x03",

            "I can't wait to meet her! ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F5B")

    label("loc_2ED2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F5B")

    ChrTalk(    #135
        0x105,
        (
            "#041FHaha! I can't imagine she'll be hard to\x01",
            "find in an outfit like that.\x02\x03",

            "I'm eager to see what kind of girl she is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8E")

    ChrTalk(    #136
        0x106,
        "#051F#7PLet's get searchin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FCF")

    label("loc_2F8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FCF")

    ChrTalk(    #137
        0x103,
        "#020F#7PLet's start to look around, shall we?\x02",
    )

    CloseMessageWindow()

    label("loc_2FCF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(430, 0, -4710, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 430, 0, -4710, 0)
    SetChrPos(0x1, 430, 0, -4710, 0)
    SetChrPos(0x2, 430, 0, -4710, 0)
    SetChrPos(0x3, 430, 0, -4710, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x160D)
    OP_28(0x89, 0x1, 0x2)
    OP_28(0x89, 0x1, 0x4)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_1E29 end

    def Function_12_3082(): pass

    label("Function_12_3082")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30B4")
    OP_8C(0xFE, 0, 300)
    OP_8C(0xFE, 270, 300)
    Sleep(1000)
    OP_8C(0xFE, 0, 300)
    OP_8C(0xFE, 90, 300)
    Sleep(1000)
    Jump("Function_12_3082")

    label("loc_30B4")

    Return()

    # Function_12_3082 end

    def Function_13_30B5(): pass

    label("Function_13_30B5")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 0, -11240, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_30DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30DC)
    OP_8E(0xFE, 0x1AE, 0x0, 0xFFFFED9A, 0x9C4, 0x0)
    Return()

    # Function_13_30B5 end

    def Function_14_30FD(): pass

    label("Function_14_30FD")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 0, -11240, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3124():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3124)
    OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0xFFFFED68, 0x9C4, 0x0)
    Return()

    # Function_14_30FD end

    def Function_15_3145(): pass

    label("Function_15_3145")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 0, -11240, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_316C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_316C)
    OP_8F(0xFE, 0xFFFFF984, 0x0, 0xFFFFEA3E, 0x9C4, 0x0)
    Return()

    # Function_15_3145 end

    def Function_16_318D(): pass

    label("Function_16_318D")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 0, -11240, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_31B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31B4)
    OP_8F(0xFE, 0x438, 0x0, 0xFFFFEAB6, 0x9C4, 0x0)
    Return()

    # Function_16_318D end

    def Function_17_31D5(): pass

    label("Function_17_31D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D4")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #138
        "\x07\x05There's a lovely podium here.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #139
        "\x07\x05Estelle peeked underneath it, but there's no one hiding there.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #140
        0x101,
        "#1019FOooh. I was so sure this was it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32EE")

    ChrTalk(    #141
        0x105,
        (
            "#048FHaha. I think she's a bit less\x01",
            "predictable than that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_32EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3342")

    ChrTalk(    #142
        0x108,
        (
            "#071FHaha! Doesn't look like we'll grab\x01",
            "her tail that easily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_3342")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3384")

    ChrTalk(    #143
        0x106,
        "#051FHeh. Guess she isn't that predictable.\x02",
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_3384")


    ChrTalk(    #144
        0x103,
        (
            "#027FLooks like we have a clever\x01",
            "little kitten on our hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C6")

    EventEnd(0x1)
    OP_A2(0x1610)
    OP_28(0x89, 0x1, 0x20)
    Jump("loc_3469")

    label("loc_33D4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #145
        "\x07\x05There's a lovely podium here.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #146
        "\x07\x05Estelle peeked underneath it, but there's no one hiding there.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_3469")

    Return()

    # Function_17_31D5 end

    def Function_18_346A(): pass

    label("Function_18_346A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_347D")
    Call(0, 19)

    label("loc_347D")

    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x9, 0xFF)
    AddParty(0x0, 0xF6, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3498")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_349C")

    label("loc_3498")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_349C")

    OP_4A(0x9, 255)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, -930, 0, 66950, 90)
    SetChrPos(0xF7, -1030, 0, 65950, 90)
    SetChrPos(0x9, 1000, 0, 66810, 270)
    SetChrFlags(0xD, 0x80)
    OP_6D(1460, 0, 74990, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_3565():
        OP_6D(720, 0, 67490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3565)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #147
        0x9,
        (
            "#702FI see... This report is very thorough.\x02\x03",

            "#701FThank you very much.\x01",
            "You investigated this quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1015F#6PI guess...\x02\x03",

            "I'm still kind of miffed we couldn't find\x01",
            "out who sent the letters, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x9,
        (
            "#701FThis is more than enough information for\x01",
            "an initial investigation.\x02\x03",

            "I doubted we'd uncover the party\x01",
            "responsible for the threats at this stage,\x01",
            "anyway.\x02\x03",

            "If anything, this gave me exactly what\x01",
            "I needed: information to consider what\x01",
            "we might need to defend against.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_37CD")

    ChrTalk(    #150
        0x106,
        (
            "#051FGood to hear.\x02\x03",

            "So what's been happening with you\x01",
            "army guys since then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3817")

    label("loc_37CD")


    ChrTalk(    #151
        0x103,
        (
            "#020FThank you, Colonel.\x02\x03",

            "So, how have your preparations\x01",
            "been going?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3817")


    ChrTalk(    #152
        0x9,
        (
            "#701FWe finished our initial deployment\x01",
            "yesterday.\x02\x03",

            "We will be using the villa as a patrol\x01",
            "headquarters until the signing ceremony\x01",
            "is concluded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#1006F#6PSo that's why there were so many soldiers\x01",
            "out and about.\x02\x03",

            "And I'm guessing that's why there were,\x01",
            "like, no monsters on the road over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "#701FWe conducted an extensive monster-\x01",
            "hunting sweep this morning.\x02\x03",

            "We'll be performing them periodically\x01",
            "until the ceremony ends.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3A0B")

    ChrTalk(    #155
        0x106,
        (
            "#053FToo bad you can't do that\x01",
            "more often...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5B")

    label("loc_3A0B")


    ChrTalk(    #156
        0x103,
        (
            "#027FWhy, Colonel, keep doing that and you\x01",
            "might just put us out of a job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5B")


    ChrTalk(    #157
        0x9,
        (
            "#701FHaha... Well, you have something of a\x01",
            "point.\x02\x03",

            "#702FSpeaking of civilian concerns.\x01",
            "About that girl's parents, the ones you\x01",
            "mentioned yesterday...\x02\x03",

            "I haven't heard any reports that they've\x01",
            "gone through any of the regional gate\x01",
            "posts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#1015F#6PNuts. Nothing to do but wait,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x9,
        (
            "#701FI will let the guild know the instant\x01",
            "we hear anything.\x02\x03",

            "For the moment, you've done fine work\x01",
            "with this investigation.\x02\x03",

            "I'll have your payment wired to the guild\x01",
            "a.s.a.p.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#1006F#6PThanks, Colonel Cid!\x02\x03",

            "#1015FBut, uh...what should we do now?\x02\x03",

            "You want us to help out with the patrols\x01",
            "in the capital once we get back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x9,
        (
            "#700FWell, if you plan on staying in Grancel,\x01",
            "I wouldn't turn away the help.\x02\x03",

            "#703FI do know you're very busy with...\x01",
            "other matters, however.\x02\x03",

            "I won't insist on you staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#1015F#6PHmmmm...\x02\x03",

            "#1006FWell, we still have Renne's situation to\x01",
            "deal with, so we'll talk to Elnan about\x01",
            "it all when we get back.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3E31")

    ChrTalk(    #163
        0x106,
        "#051FSounds like a plan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E5F")

    label("loc_3E31")


    ChrTalk(    #164
        0x103,
        "#020FYes, that seems like the best idea.\x02",
    )

    CloseMessageWindow()

    label("loc_3E5F")

    OP_4A(0xA, 255)
    SetChrPos(0xA, 970, 0, 58600, 0)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #165
        0xA,
        "Man's Voice",
        "#1PSir! Excuse me, sir!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3EC4():
        OP_6D(850, 0, 67000, 1000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3EC4)

    def lambda_3EDC():
        OP_8E(0xFE, 0x406, 0x0, 0xFF8C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3EDC)

    def lambda_3EF7():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EF7)
    Sleep(50)

    def lambda_3F0A():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3F0A)
    Sleep(50)

    def lambda_3F1D():

        label("loc_3F1D")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_3F1D")

    QueueWorkItem2(0x101, 2, lambda_3F1D)

    def lambda_3F2E():

        label("loc_3F2E")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_3F2E")

    QueueWorkItem2(0xF7, 2, lambda_3F2E)

    def lambda_3F3F():

        label("loc_3F3F")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_3F3F")

    QueueWorkItem2(0x9, 1, lambda_3F3F)
    WaitChrThread(0xA, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0x9, 0x1)
    OP_8C(0x101, 90, 0)

    ChrTalk(    #166
        0x9,
        "#702FBelc, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        "Er...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 315, 400)
    Sleep(500)
    OP_8C(0xA, 0, 400)
    Sleep(500)

    ChrTalk(    #168
        0x9,
        "#701FDon't worry, these people can be trusted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xA,
        "Very well, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "We've received a phone transmission from\x01",
            "headquarters at Leiston, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "Remnants of the Intelligence Division have\x01",
            "been sighted in the Bose region!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #172
        0x101,
        "#1020FWhat?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_410B")

    ChrTalk(    #173
        0x106,
        "#052FNo way!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4125")

    label("loc_410B")


    ChrTalk(    #174
        0x103,
        "#023FYou're kidding!\x02",
    )

    CloseMessageWindow()

    label("loc_4125")


    ChrTalk(    #175
        0x9,
        "#700FDetails, man. Explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        "They were first sighted by some bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        (
            "I'm afraid we don't have all the details\x01",
            "on their confrontation yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "However, General Bright has ordered all\x01",
            "army stations to stand by at level 2 alert!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        "#703FI see. Thank you, Mr. Belc.\x02",
    )

    CloseMessageWindow()

    def lambda_4243():
        OP_6D(720, 0, 67490, 1000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4243)
    TurnDirection(0x9, 0x101, 400)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #180
        0x9,
        (
            "#700FI suspect...we're going to be\x01",
            "busy fairly soon.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4300")

    ChrTalk(    #181
        0x106,
        "#053FYeah, no kidding.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 0, 400)

    ChrTalk(    #182
        0x106,
        (
            "#050F#2PEstelle. Back to the guild,\x01",
            "on the double.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4361")

    label("loc_4300")


    ChrTalk(    #183
        0x103,
        "#020FSeems like it...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    ChrTalk(    #184
        0x103,
        (
            "#022F#2PEstelle, we should get back to\x01",
            "the guild at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4361")

    OP_8C(0x101, 180, 400)

    ChrTalk(    #185
        0x101,
        "#1002F#6PRight!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    OP_8C(0xF7, 90, 400)

    ChrTalk(    #186
        0x101,
        "#1006F#6PColonel Cid, good luck with your patrols and stuff!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x9,
        "#701FStay safe, friends.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(10, 0, 61900, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, 900, 0, 66800, 270)
    SetChrPos(0xA, -840, 0, 66800, 90)
    SetChrPos(0x101, 10, 0, 61900, 180)
    SetChrPos(0xF7, 10, 0, 61900, 180)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_A2(0x162A)
    OP_28(0x8B, 0x1, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4498")
    OP_28(0x8A, 0x1, 0x20)
    Jump("loc_44A5")

    label("loc_4498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_44A5")
    OP_28(0x8A, 0x1, 0x10)

    label("loc_44A5")

    OP_28(0x8A, 0x1, 0x40)
    OP_28(0x8A, 0x1, 0x80)
    OP_28(0x8A, 0x1, 0x100)
    OP_28(0xC4, 0x4, 0x40)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_18_346A end

    def Function_19_44CD(): pass

    label("Function_19_44CD")

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
        (0, "loc_4546"),
        (1, "loc_454C"),
        (SWITCH_DEFAULT, "loc_4552"),
    )


    label("loc_4546")

    OP_A2(0x1200)
    Jump("loc_4552")

    label("loc_454C")

    OP_A2(0x1201)
    Jump("loc_4552")

    label("loc_4552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4560")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4564")

    label("loc_4560")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4564")

    Return()

    # Function_19_44CD end

    def Function_20_4565(): pass

    label("Function_20_4565")

    ClearMapFlags(0x1)
    OP_6D(-3960, 0, -27940, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_45A8")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_45C6")

    label("loc_45A8")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_45C6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_20_4565 end

    SaveToFile()

Try(main)
