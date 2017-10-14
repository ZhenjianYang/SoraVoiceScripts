from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T2300   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2300.x',
        MapIndex            = 86,
        MapDefaultBGM       = "ed60015",
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
        'Sadie',                                # 9
        'Lucia',                                # 10
        'Elder Serge',                          # 11
        'Manoria Byroad',                       # 12
        'Gull Seaside Way',                     # 13
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
        'ED6_DT07/CH01150 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01150P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 0,
        Y                   = 23500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 4000,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 38210,
        Z                   = -50,
        Y                   = 17840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 7990,
        Y                   = 68620,
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
        X                   = 75410,
        Z                   = -40,
        Y                   = 20810,
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


    DeclEvent(
        X                   = 16870,
        Y                   = 7000,
        Z                   = -7690,
        Range               = -9400,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFFD80,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 27540,
        Y                   = 0,
        Z                   = 18980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 53410,
        Y                   = 0,
        Z                   = 22710,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4000,
        Z                   = 20210,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = 4450,
        TriggerZ            = 6500,
        TriggerY            = -2640,
        TriggerRange        = 800,
        ActorX              = 4450,
        ActorZ              = 7500,
        ActorY              = -2740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 37440,
        TriggerZ            = -10,
        TriggerY            = 19280,
        TriggerRange        = 800,
        ActorX              = 37440,
        ActorZ              = 1500,
        ActorY              = 18980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38140,
        TriggerZ            = -40,
        TriggerY            = 10680,
        TriggerRange        = 1000,
        ActorX              = 38310,
        ActorZ              = -1540,
        ActorY              = 7000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24E",          # 00, 0
        "Function_1_2C2",          # 01, 1
        "Function_2_32C",          # 02, 2
        "Function_3_5C9",          # 03, 3
        "Function_4_C0B",          # 04, 4
        "Function_5_10D1",         # 05, 5
        "Function_6_159C",         # 06, 6
        "Function_7_15F7",         # 07, 7
        "Function_8_1CE3",         # 08, 8
        "Function_9_2355",         # 09, 9
        "Function_10_2669",        # 0A, 10
        "Function_11_2701",        # 0B, 11
        "Function_12_27A0",        # 0C, 12
        "Function_13_28AA",        # 0D, 13
        "Function_14_28AE",        # 0E, 14
        "Function_15_28B2",        # 0F, 15
    )


    def Function_0_24E(): pass

    label("Function_0_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_269")
    SetChrPos(0x9, 15050, 3980, 22520, 161)
    Jump("loc_298")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_273")
    Jump("loc_298")

    label("loc_273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_27D")
    Jump("loc_298")

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_287")
    Jump("loc_298")

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_298")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_298")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_2A4"),
        (SWITCH_DEFAULT, "loc_2C1"),
    )


    label("loc_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BE")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_2BE")

    Jump("loc_2C1")

    label("loc_2C1")

    Return()

    # Function_0_24E end

    def Function_1_2C2(): pass

    label("Function_1_2C2")

    OP_16(0x2, 0xFA0, 0xFFFE5A20, 0xFFFE13D0, 0x23004B)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_2E9")
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_304")
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x1)
    OP_71(0x7, 0x4)
    OP_64(0x1, 0x1)

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_321")
    OP_72(0x2, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x2, 0x10)
    OP_64(0x0, 0x1)
    Jump("loc_32B")

    label("loc_321")

    OP_71(0x2, 0x4)
    OP_72(0x8, 0x10)

    label("loc_32B")

    Return()

    # Function_1_2C2 end

    def Function_2_32C(): pass

    label("Function_2_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_359")

    label("loc_333")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_356")
    OP_8D(0xFE, 16309, 21410, 13470, 24720, 3000)
    Jump("loc_333")

    label("loc_356")

    Jump("loc_5C8")

    label("loc_359")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C")
    Return()

    label("loc_36C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    SetChrPos(0xFE, 45290, -10, 21290, 0)
    OP_8E(0xFE, 0x9A24, 0xFFFFFF88, 0x3E76, 0xDAC, 0x0)
    OP_8E(0xFE, 0x1428, 0xFA0, 0x3B42, 0xDAC, 0x0)
    Jump("loc_424")

    label("loc_3B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
    SetChrPos(0xFE, 5130, 4030, 10940, 0)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0xBD6, 0xFBE, 0x32DC, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_424")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C8")
    OP_8E(0xFE, 0x1428, 0xFA0, 0x3B42, 0xDAC, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x1B80, 0xFBE, 0x323C, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0x140A, 0xFBE, 0x2ABC, 0xDAC, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0xFE, 0xBD6, 0xFBE, 0x32DC, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C5")
    OP_8E(0xFE, 0x9A24, 0xFFFFFF88, 0x3E76, 0xDAC, 0x0)
    OP_8E(0xFE, 0xB0EA, 0xFFFFFFF6, 0x532A, 0xDAC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E")
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_54E")

    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 180, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59B")
    OP_62(0x8, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)

    label("loc_59B")

    Sleep(1500)
    OP_8C(0xFE, 250, 400)
    OP_8E(0xFE, 0x9A24, 0xFFFFFF88, 0x3E76, 0xDAC, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C5")

    Jump("loc_424")

    label("loc_5C8")

    Return()

    # Function_2_32C end

    def Function_3_5C9(): pass

    label("Function_3_5C9")

    OP_A2(0x2)
    TalkBegin(0x8)
    OP_63(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2")
    OP_0D()
    OP_A9(0x71)
    OP_56(0x0)
    TalkEnd(0x8)
    OP_A3(0x2)
    Return()

    label("loc_5F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_606")
    TalkEnd(0x8)
    OP_A3(0x2)
    Return()

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_731")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C7")

    ChrTalk(    #0
        0x8,
        (
            "We're having a rough time without\x01",
            "the use orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "Grandma's not bothered at all, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "The knowledge and experience of\x01",
            "the elderly really is incredible.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_72E")

    label("loc_6C7")


    ChrTalk(    #3
        0x8,
        (
            "Grandma doesn't care a whit that\x01",
            "we can't use orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "She's tougher than a turtle's shell.\x02",
    )

    CloseMessageWindow()

    label("loc_72E")

    Jump("loc_C04")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7DB")

    ChrTalk(    #5
        0x8,
        (
            "An army patrol ship made an emergency\x01",
            "landing on the beach nearby, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "There was someone injured there,\x01",
            "so they're resting at the lodge here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04")

    label("loc_7DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_8CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_841")

    ChrTalk(    #7
        0x8,
        "I was just a child last time, so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "For me, this election is my first one.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CA")

    label("loc_841")

    OP_A2(0x0)

    ChrTalk(    #9
        0x8,
        (
            "I'll be voting for the first\x01",
            "time in this election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "I intend to vote after carefully considering\x01",
            "the candidate's character.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CA")

    Jump("loc_C04")

    label("loc_8CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_95C")

    ChrTalk(    #11
        0x8,
        "Welcome, would you like some flowers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "They're not just for looking at, you know.\x01",
            "Some flowers you can use in recipes,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04")

    label("loc_95C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_A9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9D7")

    ChrTalk(    #13
        0x8,
        (
            "The children have completely regained\x01",
            "their cheer, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "I knew Aidios would watch over us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A98")

    label("loc_9D7")

    OP_A2(0x0)

    ChrTalk(    #15
        0x8,
        (
            "The children have completely regained\x01",
            "their cheer, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "I wasn't sure how things would\x01",
            "turn out after the orphanage fire,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "I knew Aidios would watch over everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_A98")

    Jump("loc_C04")

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_B66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B04")

    ChrTalk(    #18
        0x8,
        "The sun's already risen quite high.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "It's about time for Sunday School to end.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B63")

    label("loc_B04")

    OP_A2(0x0)

    ChrTalk(    #20
        0x8,
        "Oh, the sun's already risen quite high.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "It's about time for Sunday School to end.\x02",
    )

    CloseMessageWindow()

    label("loc_B63")

    Jump("loc_C04")

    label("loc_B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_C04")

    ChrTalk(    #22
        0x8,
        (
            "A...priest passed by a bit ago. At least,\x01",
            "I think he was a priest. He had the\x01",
            "weirdest clothes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "I wonder if he's the new traveling priest.\x02",
    )

    CloseMessageWindow()

    label("loc_C04")

    OP_A3(0x2)
    TalkEnd(0x8)
    Return()

    # Function_3_5C9 end

    def Function_4_C0B(): pass

    label("Function_4_C0B")

    TalkBegin(0xFE)
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_D10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB3")

    ChrTalk(    #24
        0xFE,
        (
            "I wanna go play with everyone from\x01",
            "the orphanage, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "Mommy said I can't yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "She said there's lots of scaaaaary monsters.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_D0D")

    label("loc_CB3")


    ChrTalk(    #27
        0xFE,
        "Mommy said I can't go out of town.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "She said there's lots of scaaaaary monsters.\x02",
    )

    CloseMessageWindow()

    label("loc_D0D")

    Jump("loc_10CD")

    label("loc_D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAB")

    ChrTalk(    #29
        0xFE,
        "I'm not just playin', you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "I'm searching for branches like Mommy asked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Ummm, are there any good branches around?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_E05")

    label("loc_DAB")


    ChrTalk(    #32
        0xFE,
        "I'm searching for branches like Mommy asked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Heehee! I'm a good girl, aren't I?\x02",
    )

    CloseMessageWindow()

    label("loc_E05")

    Jump("loc_10CD")

    label("loc_E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_E76")

    ChrTalk(    #34
        0xFE,
        (
            "Heehee, I hope I can go to\x01",
            "Sunday School again soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "I'm playing outside lots with Polly!\x02",
    )

    CloseMessageWindow()
    Jump("loc_10CD")

    label("loc_E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EB6")

    ChrTalk(    #36
        0xFE,
        (
            "I wonder why the old guy\x01",
            "doesn't go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F52")

    label("loc_EB6")

    OP_A2(0x1)

    ChrTalk(    #37
        0xFE,
        (
            "Our place is a bar, but there's a reeeally,\x01",
            "really drunk customer there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "He's a real old guy, but it seems like\x01",
            "something really bad happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F52")

    Jump("loc_10CD")

    label("loc_F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_10CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106E")
    TurnDirection(0xFE, 0x109, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FB7")

    ChrTalk(    #39
        0xFE,
        (
            "Mr. Kevin, next time you come\x01",
            "read me a book, pleeease.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106B")

    label("loc_FB7")

    OP_A2(0x1)

    ChrTalk(    #40
        0xFE,
        "Oooh, Mr. Kevin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Mr. Kevin, read me another book, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1062FYeah, you leave it to me, kiddo.\x02\x03",

            "You be a good girl, too, Lucia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Yeah, okay! I'll be waiting.\x02",
    )

    CloseMessageWindow()

    label("loc_106B")

    Jump("loc_10CD")

    label("loc_106E")


    ChrTalk(    #44
        0xFE,
        "The teacher today was a fun person. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "Ehe, I can't wait for the next Sunday School.\x02",
    )

    CloseMessageWindow()

    label("loc_10CD")

    TalkEnd(0xFE)
    Return()

    # Function_4_C0B end

    def Function_5_10D1(): pass

    label("Function_5_10D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_125F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_11AB")

    ChrTalk(    #46
        0xFE,
        (
            "The nobleman who was the previous mayor\x01",
            "was arrested, and now commoner candidates\x01",
            "are competing to take up after him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "This election almost seems like it\x01",
            "represents the changing of an age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125C")

    label("loc_11AB")

    OP_A2(0x3)

    ChrTalk(    #48
        0xFE,
        (
            "Norman and Portos are both commoners,\x01",
            "but they are also both great people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "The old elections used to be reserved for\x01",
            "nobility, but it seems the times have changed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125C")

    Jump("loc_1598")

    label("loc_125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_13AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_12F8")

    ChrTalk(    #50
        0xFE,
        "Last election, this was the voting site.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Many people believed in the name of\x01",
            "the Dalmore family as they put in\x01",
            "their votes...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_12F8")

    OP_A2(0x3)

    ChrTalk(    #52
        0xFE,
        "Last election, this was the voting site but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "...No matter how you\x01",
            "look at it it's too small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I guess I have to ask The White Magnolia\x01",
            "inn for a bit of help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A9")

    Jump("loc_1598")

    label("loc_13AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_1435")

    ChrTalk(    #55
        0xFE,
        (
            "The youth of the village went to help\x01",
            "rebuild the orphanage, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I hope their hearts stay as generous forever.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1598")

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1598")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_14D8")

    ChrTalk(    #57
        0xFE,
        (
            "The trouble the last mayor caused was\x01",
            "a serious blow to Manoria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "After terrible incidents like that, tourists\x01",
            "stay far away, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1598")

    label("loc_14D8")

    OP_A2(0x3)

    ChrTalk(    #59
        0xFE,
        "Oh, travelers. Welcome to Manoria.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "The orphanage has been rebuilt,\x01",
            "and people have returned to their\x01",
            "normal lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Now we just have to wait for\x01",
            "our next mayor to be elected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1598")

    TalkEnd(0xFE)
    Return()

    # Function_5_10D1 end

    def Function_6_159C(): pass

    label("Function_6_159C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_15AD")
    TalkEnd(0xFF)
    Call(0, 9)
    Jump("loc_15F6")

    label("loc_15AD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #62
        "\x07\x05Sunday School: In Session\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_15F6")

    Return()

    # Function_6_159C end

    def Function_7_15F7(): pass

    label("Function_7_15F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1608")
    Call(0, 10)

    label("loc_1608")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 64319, 0, 21000, 270)
    SetChrPos(0xF7, 64170, 0, 19800, 270)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6C(45000, 0)
    OP_C8(0x200, 0x46, "C_PLAC06._CH", 0x0, 0x7D0)
    OP_DE("Manoria")
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_182C")

    ChrTalk(    #63
        0x106,
        (
            "#050F#4PAnd here's Manoria. Haven't been here\x01",
            "since that whole 'stolen donations' thing.\x02\x03",

            "Still quiet as a church, it looks like.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #64
        0x101,
        (
            "#1006F#3PHey, nothing wrong with that.\x01",
            "I like it!\x02\x03",

            "Your hometown of Ravennue was\x01",
            "pretty quiet too, if I remember right.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #65
        0x106,
        (
            "#552F#4PI guess...\x02\x03",

            "#053FAnyway. Kids should be at Sunday\x01",
            "School somewhere in the village.\x02\x03",

            "Let's look for 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC8")

    label("loc_182C")


    ChrTalk(    #66
        0x103,
        (
            "#021F#4PAh, Manoria. It feels like a dog's\x01",
            "age since I was here last.\x02\x03",

            "#020FCome to think of it, I don't really get\x01",
            "out to Ruan in general all that much.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #67
        0x101,
        (
            "#1004F#3PYou don't? Huh.\x02\x03",

            "I always figured you and Dad went\x01",
            "all over the place, not just Rolent.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #68
        0x103,
        (
            "#020F#4PI mostly keep to Rolent, to be honest.\x02\x03",

            "I go out to Bose and Grancel often\x01",
            "enough, mind, but that's about it.\x02\x03",

            "The only ones I can think of with\x01",
            "absolutely no 'roots' would be your\x01",
            "father as a bracer...and Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1011F#3POh. Yeah, Agate does kind\x01",
            "of strike me as a wanderer.\x02\x03",

            "#1015FI don't think I've ever seen him\x01",
            "in Rolent, though...or have I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#027F#4PMm-hmm. I think he tends to avoid Rolent\x01",
            "since, well, Cassius lives there.\x02\x03",

            "He has some, ah...issues with\x01",
            "Cassius that make it a bit hard\x01",
            "for them to work together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1016F#3PIssues, huh? Haha. I think I get it.\x02\x03",

            "#1017FI wonder how Agate and Anelace\x01",
            "are doing, come to think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#020F#4PThey just started investigating, too.\x01",
            "I doubt they're all that far 'ahead' of\x01",
            "us.\x02\x03",

            "#021FAll right! The children should be\x01",
            "in Sunday School around here... \x01",
            "somewhere.\x02\x03",

            "Let's poke around a bit and figure\x01",
            "out where that would be, hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC8")


    ChrTalk(    #73
        0x101,
        "#1006F#3PRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1218)
    EventEnd(0x0)
    Return()

    # Function_7_15F7 end

    def Function_8_1CE3(): pass

    label("Function_8_1CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 1)), scpexpr(EXPR_END)), "loc_1CEB")
    Return()

    label("loc_1CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D05")
    Call(0, 10)
    FadeToBright(0, 0)

    label("loc_1D05")

    EventBegin(0x0)
    OP_8C(0x0, 180, 0)
    OP_8C(0x1, 180, 0)

    ChrTalk(    #74
        0x101,
        "#1026FOh...\x02",
    )

    CloseMessageWindow()
    OP_82(0x85, 0x0)

    def lambda_1D2F():
        OP_6D(2428, 6000, -13190, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D2F)

    def lambda_1D47():
        OP_6B(8450, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D47)

    def lambda_1D57():
        OP_6C(60000, 7000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1D57)

    def lambda_1D67():
        OP_67(0, 5095, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1D67)
    StopSound(0x186A0, 0x3D090, 0x1B58)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 5180, 6000, -10280, 180)
    SetChrPos(0xF7, 6160, 6000, -8180, 180)
    OP_6D(5470, 6010, -12430, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_67(0, 8140, -10000, 0)
    StopSound(0x0, 0x0, 0x0)
    Sleep(500)

    def lambda_1E04():
        OP_8E(0x101, 0x143C, 0x177A, 0xFFFFCEDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E04)

    def lambda_1E1F():
        OP_8E(0xF7, 0x1810, 0x1770, 0xFFFFCEF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1E1F)
    FadeToBright(1000, 0)
    WaitChrThread(0xF7, 0x1)
    OP_AD(0x24002A, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x3E8)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        "#1025FThis is...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1EAC")
    TurnDirection(0x106, 0x101, 400)
    Sleep(500)

    ChrTalk(    #76
        0x106,
        "#052F#4PHuh? What's up?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EDC")

    label("loc_1EAC")

    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #77
        0x103,
        "#023F#4PEstelle? What's wrong?\x02",
    )

    CloseMessageWindow()

    label("loc_1EDC")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #78
        0x101,
        (
            "#1016FOh, uh, haha...\x02\x03",

            "Umm, Joshua and I had lunch here\x01",
            "a while back, you see...\x02\x03",

            "#1025FIt just...came back to me, is all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F87")

    ChrTalk(    #79
        0x106,
        "#552F#4PAh, right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F9E")

    label("loc_1F87")


    ChrTalk(    #80
        0x103,
        "#522F#4P...I see.\x02",
    )

    CloseMessageWindow()

    label("loc_1F9E")


    ChrTalk(    #81
        0x101,
        (
            "#1008FHey, don't be like that. It's not like\x01",
            "it's a memory of some great tragedy\x01",
            "or anything.\x02\x03",

            "#1007FI was just a kid who didn't really\x01",
            "understand her own feelings.\x02\x03",

            "I totally forced Joshua to let me feed\x01",
            "him, not even caring if anyone saw...\x02\x03",

            "He must've been really sick of me,\x01",
            "even then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_211E")

    ChrTalk(    #82
        0x106,
        (
            "#051F#4PHeh. You're still a kid if you ask me.\x02\x03",

            "How 'bout it? Need a sec?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A4")

    label("loc_211E")


    ChrTalk(    #83
        0x103,
        (
            "#021F#4PHmm... Introspection?\x01",
            "Very unlike you, Estelle. However...\x01",
            "I like it.\x02\x03",

            "#027FDo you need a moment? We can\x01",
            "spare the time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_2225")

    ChrTalk(    #84
        0x101,
        (
            "#1012FNo. I can't stop now.\x01",
            "Can't let myself stop now.\x02\x03",

            "#1011FBesides! We need to find that\x01",
            "Sunday School, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D9")

    label("loc_2225")


    ChrTalk(    #85
        0x101,
        (
            "#1012FNo. I can't stop now.\x01",
            "Can't let myself stop now.\x02\x03",

            "#1011FBesides! We need to head over\x01",
            "to the orphanage.\x02\x03",

            "I want to see Matron Theresa and ask\x01",
            "about this 'white shadow.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2301")

    ChrTalk(    #86
        0x106,
        "#051F#4PRight. Let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_231A")

    label("loc_2301")


    ChrTalk(    #87
        0x103,
        "#020F#4PWell, then.\x02",
    )

    CloseMessageWindow()

    label("loc_231A")

    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A2(0x1219)
    EventEnd(0x0)
    Return()

    # Function_8_1CE3 end

    def Function_9_2355(): pass

    label("Function_9_2355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_236F")
    Call(0, 10)
    FadeToBright(0, 0)

    label("loc_236F")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 5780, 6000, -2110, 266)
    SetChrPos(0xF7, 5900, 6000, -3190, 271)
    OP_6D(4140, 6480, -3460, 0)
    OP_67(0, 8060, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(245000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #88
        "\x07\x05Sunday School: Class In Session\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #89
        0x101,
        (
            "#1011FOh, hey! Here's the Sunday School.\x02\x03",

            "#1015FGiven that the sign's still up,\x01",
            "I guess they're still in class?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2522")

    ChrTalk(    #90
        0x106,
        (
            "#051F#5PCould be. Let's take a look inside.\x02\x03",

            "They might've finished for the day and\x01",
            "just forgot to take down the sign, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2595")

    label("loc_2522")


    ChrTalk(    #91
        0x103,
        (
            "#020F#5PShall we poke our noses in?\x02\x03",

            "They might've ended for the day and\x01",
            "simply forgot to take the sign down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2595")


    ChrTalk(    #92
        0x101,
        "#1006FGood idea! Let me take a peek.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x11BC, 0x1946, 0xFFFFF736, 0x7D0, 0x0)
    OP_8C(0x101, 270, 0)
    Sleep(500)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x3)
    Sleep(1000)

    ChrTalk(    #93
        0x101,
        "#1015F(Oooookay, lesse...)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #94
        0x101,
        "#1004F(W-Wait a sec! I know that guy...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2355 end

    def Function_10_2669(): pass

    label("Function_10_2669")

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
        (0, "loc_26E2"),
        (1, "loc_26E8"),
        (SWITCH_DEFAULT, "loc_26EE"),
    )


    label("loc_26E2")

    OP_A2(0x1200)
    Jump("loc_26EE")

    label("loc_26E8")

    OP_A2(0x1201)
    Jump("loc_26EE")

    label("loc_26EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_26FC")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_2700")

    label("loc_26FC")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_2700")

    Return()

    # Function_10_2669 end

    def Function_11_2701(): pass

    label("Function_11_2701")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #95
        (
            "\x07\x05《Ruan Mayoral Election》※ Make sure to go to the voting site\x01",
            "on voting day! -Election Management Committee\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_2701 end

    def Function_12_27A0(): pass

    label("Function_12_27A0")

    EventBegin(0x1)

    ChrTalk(    #96
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_27CC():
        OP_6D(38050, -50, 9240, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_27CC)

    def lambda_27E4():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_27E4)

    def lambda_27F4():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_27F4)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #97
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289A")
    OP_C0(0xE, 0x15, 0x94FC, 0xFFFFFFD8, 0x29B8, 0xB4, 0x95A6, 0xFFFFF9FC, 0x1B58)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_28A9")

    label("loc_289A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A9")
    EventEnd(0x1)

    label("loc_28A9")

    Return()

    # Function_12_27A0 end

    def Function_13_28AA(): pass

    label("Function_13_28AA")

    SetPlaceName(0x58)
    Return()

    # Function_13_28AA end

    def Function_14_28AE(): pass

    label("Function_14_28AE")

    SetPlaceName(0x57)
    Return()

    # Function_14_28AE end

    def Function_15_28B2(): pass

    label("Function_15_28B2")

    SetPlaceName(0x59)
    Return()

    # Function_15_28B2 end

    SaveToFile()

Try(main)
