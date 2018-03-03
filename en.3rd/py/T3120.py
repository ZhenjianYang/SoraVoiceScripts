from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3120   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3120   ._SN',
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
        'Kilika',                               # 9
        'Tita',                                 # 10
        'Erika',                                # 11
        'Elwyn',                                # 12
        'Elkan',                                # 13
        'Ada',                                  # 14
        'Didi',                                 # 15
        'Wong',                                 # 16
        'Gundolf',                              # 17
        'Target Camera',                        # 18
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
        'ED6_DT07/CH02610 ._CH',             # 00
        'ED6_DT07/CH02020 ._CH',             # 01
        'ED6_DT07/CH00060 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00040 ._CH',             # 05
        'ED6_DT07/CH00033 ._CH',             # 06
        'ED6_DT07/CH00043 ._CH',             # 07
        'ED6_DT07/CH02620 ._CH',             # 08
        'ED6_DT07/CH00070 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01030 ._CH',             # 0C
        'ED6_DT07/CH01160 ._CH',             # 0D
        'ED6_DT07/CH01760 ._CH',             # 0E
        'ED6_DT07/CH00023 ._CH',             # 0F
        'ED6_DT07/CH00053 ._CH',             # 10
        'ED6_DT07/CH00063 ._CH',             # 11
        'ED6_DT07/CH00073 ._CH',             # 12
        'ED6_DT07/CH01040 ._CH',             # 13
        'ED6_DT07/CH02490 ._CH',             # 14
        'ED6_DT27/CH03970 ._CH',             # 15
        'ED6_DT06/CH20137 ._CH',             # 16
        'ED6_DT07/CH01750 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH02610P._CP',             # 00
        'ED6_DT07/CH02020P._CP',             # 01
        'ED6_DT07/CH00060P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00040P._CP',             # 05
        'ED6_DT07/CH00033P._CP',             # 06
        'ED6_DT07/CH00043P._CP',             # 07
        'ED6_DT07/CH02620P._CP',             # 08
        'ED6_DT07/CH00070P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01030P._CP',             # 0C
        'ED6_DT07/CH01160P._CP',             # 0D
        'ED6_DT07/CH01760P._CP',             # 0E
        'ED6_DT07/CH00023P._CP',             # 0F
        'ED6_DT07/CH00053P._CP',             # 10
        'ED6_DT07/CH00063P._CP',             # 11
        'ED6_DT07/CH00073P._CP',             # 12
        'ED6_DT07/CH01040P._CP',             # 13
        'ED6_DT07/CH02490P._CP',             # 14
        'ED6_DT27/CH03970P._CP',             # 15
        'ED6_DT06/CH20137P._CP',             # 16
        'ED6_DT07/CH01750P._CP',             # 17
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 1200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1780,
        Z                   = 1000,
        Y                   = 53000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 52970,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 52390,
        Z                   = 0,
        Y                   = 53790,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55570,
        Z                   = 0,
        Y                   = 51740,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 25480,
        Z                   = 0,
        Y                   = -3020,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 51290,
        Z                   = 4000,
        Y                   = 410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -1320,
        TriggerZ            = 0,
        TriggerY            = -4700,
        TriggerRange        = 1400,
        ActorX              = -1320,
        ActorZ              = 2000,
        ActorY              = -4700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = 0,
        TriggerY            = -710,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 1200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1830,
        TriggerZ            = 1000,
        TriggerY            = 51000,
        TriggerRange        = 400,
        ActorX              = 1780,
        ActorZ              = 2500,
        ActorY              = 53000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53210,
        TriggerZ            = 0,
        TriggerY            = 520,
        TriggerRange        = 400,
        ActorX              = 52970,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_33A",          # 00, 0
        "Function_1_3A7",          # 01, 1
        "Function_2_3A8",          # 02, 2
        "Function_3_44F",          # 03, 3
        "Function_4_473",          # 04, 4
        "Function_5_478",          # 05, 5
        "Function_6_5D6",          # 06, 6
        "Function_7_786",          # 07, 7
        "Function_8_855",          # 08, 8
        "Function_9_85A",          # 09, 9
        "Function_10_B00",         # 0A, 10
        "Function_11_1268",        # 0B, 11
        "Function_12_126D",        # 0C, 12
        "Function_13_19EB",        # 0D, 13
        "Function_14_1CBD",        # 0E, 14
        "Function_15_28AC",        # 0F, 15
        "Function_16_39D2",        # 10, 16
        "Function_17_3A0E",        # 11, 17
    )


    def Function_0_33A(): pass

    label("Function_0_33A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371")
    SetChrFlags(0x18, 0x10)

    label("loc_371")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_393")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_3A6")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3A6")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_3A6")

    Return()

    # Function_0_33A end

    def Function_1_3A7(): pass

    label("Function_1_3A7")

    Return()

    # Function_1_3A7 end

    def Function_2_3A8(): pass

    label("Function_2_3A8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3D9"),
        (1, "loc_3E5"),
        (2, "loc_3F1"),
        (3, "loc_3FD"),
        (4, "loc_409"),
        (5, "loc_415"),
        (6, "loc_421"),
        (SWITCH_DEFAULT, "loc_42D"),
    )


    label("loc_3D9")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_439")

    label("loc_3E5")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_439")

    label("loc_3F1")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_439")

    label("loc_3FD")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_439")

    label("loc_409")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_439")

    label("loc_415")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_439")

    label("loc_421")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_439")

    label("loc_42D")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_439")

    label("loc_439")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_439")

    label("loc_44E")

    Return()

    # Function_2_3A8 end

    def Function_3_44F(): pass

    label("Function_3_44F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_472")
    OP_8D(0xFE, 52620, 51160, 59990, 53120, 3000)
    Jump("Function_3_44F")

    label("loc_472")

    Return()

    # Function_3_44F end

    def Function_4_473(): pass

    label("Function_4_473")

    Call(0, 5)
    Return()

    # Function_4_473 end

    def Function_5_478(): pass

    label("Function_5_478")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_5D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4F2")
    OP_8C(0x13, 180, 0)

    ChrTalk(    #0
        0x13,
        "...Where did Knowles go, anyway?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x13,
        (
            "I thought he was putting everything\x01",
            "on the shelves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D2")

    label("loc_4F2")


    ChrTalk(    #2
        0x13,
        "Hey! Welcome to Bell Station!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x13,
        (
            "If there's anything you need help with,\x01",
            "don't hesitate to let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x13,
        (
            "We're aiming for this store to be loved by the\x01",
            "community, and we'll spare no effort to make\x01",
            "that happen!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_5D2")

    TalkEnd(0x13)
    Return()

    # Function_5_478 end

    def Function_6_5D6(): pass

    label("Function_6_5D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_629")

    ChrTalk(    #5
        0xFE,
        (
            "Now I need to sort out what to order in\x01",
            "for next month...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_782")

    label("loc_629")


    ChrTalk(    #6
        0xFE,
        (
            "Daily goods are selling like wildfire this month.\x01",
            "Which is great news for us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Ever since the orbal power went out before,\x01",
            "lamps and stuff along those lines have been\x01",
            "selling like hotcakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "On the surface, everything is back to normal...\x01",
            "but it's obvious the unease in people's hearts\x01",
            "is going to take a while longer to vanish.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_782")

    TalkEnd(0xFE)
    Return()

    # Function_6_5D6 end

    def Function_7_786(): pass

    label("Function_7_786")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_851")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7DE")

    ChrTalk(    #9
        0xFE,
        "I wonder if she'll play with me tomorrow?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Probably not...\x02",
    )

    CloseMessageWindow()
    Jump("loc_851")

    label("loc_7DE")


    ChrTalk(    #11
        0xFE,
        "Tita won't play with me at all lately!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "She's always really busy with something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "It's not fair...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_851")

    TalkEnd(0xFE)
    Return()

    # Function_7_786 end

    def Function_8_855(): pass

    label("Function_8_855")

    Call(0, 9)
    Return()

    # Function_8_855 end

    def Function_9_85A(): pass

    label("Function_9_85A")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_AFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9E7")

    ChrTalk(    #14
        0x14,
        (
            "Stain's a stubborn old mule, let me tell you!\x01",
            "He absolutely refuses to allow us to stock \x01",
            "the latest weaponry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        (
            "Part of me can see where he's coming from with\x01",
            "his whole 'not as reliable' argument because they\x01",
            "haven't been proven in the long term...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x14,
        (
            "...but I still think that thing's a real beauty.\x01",
            "I'll just have to keep badgering him and pray\x01",
            "the stars line up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC")

    label("loc_9E7")


    ChrTalk(    #17
        0x14,
        (
            "The Reinford Company's working on expanding\x01",
            "their lineup at the moment, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x14,
        (
            "Personally, I'm hoping we can start selling their\x01",
            "new orbal cannon here, but who knows if that'll\x01",
            "be possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        (
            "I'll have to keep badgering the owner and pray\x01",
            "the stars line up!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_AFC")

    TalkEnd(0x14)
    Return()

    # Function_9_85A end

    def Function_10_B00(): pass

    label("Function_10_B00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_1264")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 6)), scpexpr(EXPR_END)), "loc_D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C0E")

    ChrTalk(    #20
        0xFE,
        (
            "Man! Thinking about it, though, I've been a \x01",
            "bracer for a hell of a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Dan and Cassius joined ages ago, too, but they\x01",
            "both left the guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I might even be the active bracer who's been\x01",
            "in the guild the longest now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4C")

    label("loc_C0E")


    ChrTalk(    #23
        0xFE,
        (
            "Yeeeah, I'd say we could do with stumbling upon\x01",
            "a few qualified newbies right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Speaking of which, wasn't it Cassius that scouted \x01",
            "you out to join the guild back in the day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x106,
        (
            "#555FWh-Why'd you have to go and bring that up?\x02\x03",

            "That was a long time ago! Some things are best\x01",
            "swept under the rug.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_D4C")

    Jump("loc_1264")

    label("loc_D4F")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #26
        0xFE,
        "...Hmm?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 500)
    Sleep(300)

    ChrTalk(    #27
        0xFE,
        "Well, if it isn't Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        (
            "#051FWhat's goin' on, Gundolf?\x02\x03",

            "Not often I catch you stopping off at a weapons\x01",
            "shop like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Haha. I'm not gonna be in town that much longer.\x01",
            "I'm due to leave on the next airship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Reports say it's gonna be delayed from what I hear,\x01",
            "though, so I've ended up with some time to kill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x106,
        "#051FHeh. Busy as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Not half as busy as Kurt!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Still, my workload's gonna be going up before\x01",
            "it goes down with all these bracers scattering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "First we lose Estelle and Joshua, and now we're\x01",
            "losing Kilika? We're really getting short on warm\x01",
            "bodies.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 0)), scpexpr(EXPR_END)), "loc_1077")

    ChrTalk(    #35
        0x106,
        (
            "#051FWhen have we ever NOT been short of people?\x02\x03",

            "We're just gonna have to keep our chins up until\x01",
            "some new guys come and ease our workloads.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_114B")

    label("loc_1077")


    ChrTalk(    #36
        0x106,
        (
            "#552FThe thing about Kilika leaving was true, then...\x02\x03",

            "#051FWhatever. When have we ever NOT been short\x01",
            "of people?\x02\x03",

            "We're just gonna have to keep our chins up until\x01",
            "some new guys come and ease our workloads.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114B")

    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Is it just me, or do you sound like you have\x01",
            "some specific new recruits in mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x106,
        "#556FHeh. I wouldn't go that far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "That's a shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I sure hope we do get some in soon. We could\x01",
            "use all the help we can get about now.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x18, 0x10)
    OP_A2(0x2F86)

    label("loc_1264")

    TalkEnd(0xFE)
    Return()

    # Function_10_B00 end

    def Function_11_1268(): pass

    label("Function_11_1268")

    Call(0, 12)
    Return()

    # Function_11_1268 end

    def Function_12_126D(): pass

    label("Function_12_126D")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_19E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 1)), scpexpr(EXPR_END)), "loc_1461")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_136F")

    ChrTalk(    #42
        0x10,
        (
            "#790FIf you're in a hurry, you should focus on getting\x01",
            "over to Zeiss Central Factory instead of hanging\x01",
            "around here.\x02\x03",

            "If you're not, by all means go and take care of\x01",
            "some of the work on the board, though. I'd like\x01",
            "that a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145E")

    label("loc_136F")


    ChrTalk(    #43
        0x10,
        (
            "#790FIf you're in a hurry, you should focus on getting\x01",
            "over to Zeiss Central Factory instead of hanging\x01",
            "around here.\x02\x03",

            "If you're not, by all means go and take care of\x01",
            "some of the work on the board, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x106,
        "#050FS-Sure thing...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_145E")

    Jump("loc_19E7")

    label("loc_1461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 0)), scpexpr(EXPR_END)), "loc_1639")

    ChrTalk(    #45
        0x10,
        "#792FCan I ask one favor of you, Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x106,
        (
            "#052FH-Huh?\x02\x03",

            "#051FWhat's up? I got you covered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "#790FCome over to Zeiss from time to time, all right?\x02\x03",

            "You've got plenty of free time, haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x106,
        (
            "#551FHell no! I'm a busy guy.\x02\x03",

            "#051FBut not so busy that I can't find the time\x01",
            "to drop by now and then for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "#791F...Thanks.\x02\x03",

            "I've told my successor all about you.\x02\x03",

            "Do try and get along with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x106,
        "#051FHeh. You never miss a beat, do you?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F89)
    Jump("loc_19E7")

    label("loc_1639")

    EventBegin(0x0)
    Fade(500)
    OP_4A(0x10, 255)
    SetChrPos(0x106, 3750, 0, -700, 0)
    OP_6D(2910, 0, 1060, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x10,
        "#790F#11PAgate? I thought you were in a hurry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x106,
        (
            "#052F#6PI was, but then I remembered something...\x02\x03",

            "I heard you were planning on leaving the\x01",
            "guild and returning home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#792F#11PIndeed.\x02\x03",

            "#791FThat's still the plan, but the process of getting\x01",
            "things ready for my successor has been taking\x01",
            "longer than planned.\x02\x03",

            "As things currently stand, I'll be leaving at the\x01",
            "start of next month.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #54
        0x106,
        (
            "#053F#6P...Right.\x02\x03",

            "#051FReally not gonna be the same around here\x01",
            "without you. You've done a lot for me while\x01",
            "you've been here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#794F#11PI suppose I have.\x02\x03",

            "#792FJust be sure not to get poisoned and collapse\x01",
            "again during my successor's time here.\x02\x03",

            "I could handle it, but you'd probably give them\x01",
            "nightmares.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #56
        0x106,
        "#055F#6PI-I didn't do that on PURPOSE, you know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "#791F#11PHaha...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F88)
    OP_4B(0x10, 255)
    EventEnd(0x0)

    label("loc_19E7")

    TalkEnd(0x10)
    Return()

    # Function_12_126D end

    def Function_13_19EB(): pass

    label("Function_13_19EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_1CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 2)), scpexpr(EXPR_END)), "loc_1B11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A85")

    ChrTalk(    #58
        0xFE,
        "Oh, whoops! I need to head off to Elmo soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Better get myself moving, or I'm gonna get an\x01",
            "earful from Kilika again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B0E")

    label("loc_1A85")


    ChrTalk(    #60
        0xFE,
        (
            "Gundolf mentioned that her husband's a former\x01",
            "bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "Apparently, he was a real showstopper, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Strange couple, huh?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1B0E")

    Jump("loc_1CB9")

    label("loc_1B11")


    ChrTalk(    #63
        0xFE,
        "Whoa... Agate's here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x106,
        "#051FHey, Wong. How are things?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "...I've been better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "You familiar with someone called Erika Russell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I've heard she's as much trouble as Professor\x01",
            "Russell, and I can believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Ever since she showed up in town, we've been\x01",
            "getting more requests coming in than usual.\x01",
            "You COULD call it a coincidence, but...yeeeah...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #69
        0x106,
        "#053FThat so...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F8A)

    label("loc_1CB9")

    TalkEnd(0xFE)
    Return()

    # Function_13_19EB end

    def Function_14_1CBD(): pass

    label("Function_14_1CBD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-960, 0, -2500, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, 1000, 0, -5800, 0)
    SetChrChipByIndex(0x106, 22)
    SetChrSubChip(0x106, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 1000, 0, -1260, 0)
    OP_4A(0x10, 255)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS369._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS368._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS368._CH")
    OP_C6(0x0, 0x0, -315000, -250000, 0)
    OP_C6(0x0, 0x1, 2000, 2000, 0)
    OP_C6(0x1, 0x0, -463000, -368000, 0)
    OP_C6(0x1, 0x1, 2500, 2500, 0)
    OP_C6(0x2, 0x0, -370000, -368000, 0)
    OP_C6(0x2, 0x1, 2500, 2500, 0)
    Sleep(500)
    OP_1F(0x0, 0x1F4)
    OP_C6(0x1, 0x3, -1, 100, 0)
    OP_C6(0x2, 0x3, -1, 100, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    Sleep(300)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #70
        "\x07\x00#052FWha...?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0xD5, 0x0, 0x64)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x1, 0xFF, 0x0)

    ChrTalk(    #71
        0x106,
        (
            "#057F#6P...?\x02\x03",

            "(Was that just my imagination?)\x02\x03",

            "#552F(The second I walked in the door, I felt like my\x01",
            "life was in mortal danger...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #72
        0x106,
        (
            "#050F#6P(The only person here is that researcher there,\x01",
            "so it must have been...)\x02",
        )
    )

    CloseMessageWindow()
    OP_1F(0x64, 0x7D0)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    Sleep(1000)

    NpcTalk(    #73
        0x12,
        "Researcher",
        "#5POh, my. My, my, my! What have we here?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 500)
    Sleep(300)

    NpcTalk(    #74
        0x12,
        "Researcher",
        (
            "#1458F#11PIf it isn't  A g a t e  C r o s n e r.\x02\x03",

            "#1833FHahaha... I pity you. I really do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x106,
        "#057F#6P...Come again?\x02",
    )

    CloseMessageWindow()

    def lambda_20D2():
        OP_8E(0xFE, 0x3E8, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20D2)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    NpcTalk(    #76
        0x12,
        "Researcher",
        (
            "#1833F#11PI never dreamed my target would come wandering\x01",
            "in nonchalantly while I was making the necessary\x01",
            "preparations for his execution.\x02\x03",

            "But that makes things easier for me. Now I can tell\x01",
            "you what I want directly!\x02\x03",

            "#1831FWe've prepared a most perfect place to die for\x01",
            "you over at the central factory.\x02\x03",

            "So come along! There's not a moment to waste!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x106,
        (
            "#555F#6PWho ARE you? You here to pick a fight with\x01",
            "me or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #78
        0x12,
        "Researcher",
        (
            "#1457F#11PNot at all.\x02\x03",

            "#1456FThis is a completely legitimate request \x01",
            "I've made to the guild.\x02\x03",

            "Or, more specifically, to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x106,
        (
            "#057F#6PLike hell, you did. No request like that would\x01",
            "ever get accepted here.\x02\x03",

            "#057FIf you wanna submit a request to the guild,\x01",
            "you're gonna have to come up with somethin'\x01",
            "a little better than that.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #80
        0x12,
        "Researcher",
        (
            "#1833F#11P*sigh* Oh, you pitiable flea. I figured you were a\x01",
            "little thickheaded, but I didn't think your general\x01",
            "IQ would be quite this low.\x02\x03",

            "#1835F#3S#30WYou need to be more aware of your sins!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #81
        0x106,
        (
            "#055F#6P(What does this woman have against me?)\x02\x03",

            "(Her eyes are scaring the shit outta me...)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x12,
        "Researcher",
        (
            "#1457F#11PClean out those ears of yours and listen well,\x01",
            "moron.\x02\x03",

            "#1452FThis request is about testing the capabilities of\x01",
            "the Orbal Gear by comparing it to you in a variety\x01",
            "of situations.\x02\x03",

            "Which means that by helping us, we'll be able to\x01",
            "improve it!\x02\x03",

            "#1458FHaha. And in the process, maybe the unforgivable\x01",
            "sins you've committed shall be...heheheheh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x106,
        (
            "#551F#6PJust what are you rambling on about, woman?\x02\x03",

            "#555FMaybe you didn't get the memo, but the Bracer\x01",
            "Guild exists to help people who REALLY need it.\x02\x03",

            "We don't exist to just do any old thing someone\x01",
            "feels like asking us to do.\x02\x03",

            "So I really haven't got time to be messin' around\x01",
            "with some crazy time-waster.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x12,
        "Researcher",
        (
            "#1458F#11P...\x02\x03",

            "Heehee...\x02\x03",

            "#1833FIs that the real reason you don't want\x01",
            "to do this? Or are you just scared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x106,
        "#057F#6PSay that again?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1CBD end

    def Function_15_28AC(): pass

    label("Function_15_28AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-960, 0, -2500, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, 0, 0, -4000, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, 0, -2500, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 2000, -500, -8000, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x10, 255)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #86
        0x106,
        "#054F#6PIf you want help that much--!\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)

    def lambda_2981():
        OP_6D(40, 0, -3500, 1500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2981)

    def lambda_2999():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2999)

    def lambda_29AB():
        OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_29AB)
    WaitChrThread(0x11, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_8C(0x11, 315, 500)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_2A0F():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2A0F)
    Sleep(100)
    TurnDirection(0x12, 0x11, 500)
    Sleep(300)

    ChrTalk(    #87
        0x106,
        "#052F#5P...Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x11,
        "#064F#6PA-Agate?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89 op#A op#5
        0x11,
        "#064F#6P#10AWhat are you doing with Mo--\x05\x02",
    )


    def lambda_2A89():
        OP_8E(0xFE, 0x618, 0x0, 0xFFFFF04D, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2A89)
    WaitChrThread(0x12, 0x1)

    def lambda_2AA9():
        OP_8E(0xFE, 0x618, 0x0, 0xFFFFEA48, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2AA9)
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x12, 0x106, 600)
    Sleep(300)
    CloseMessageWindow()

    NpcTalk(    #90
        0x12,
        "Researcher",
        (
            "#1458F#6POh, and one more thing I want to make\x01",
            "VERY clear right off the bat.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #91
        0x12,
        "Researcher",
        (
            "#1830F#6P#3SYou do not get within a one selge radius\x01",
            "of my sugar-powdered donut under ANY\x01",
            "circumstances!\x02",
        )
    )

    OP_7C(0x0, 0x15E, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #92
        0x12,
        "Researcher",
        "#1830F#6PAre we clear, you shameless hoodlum?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x106,
        "#052F#5PW-Wait a se...\x02",
    )

    CloseMessageWindow()

    def lambda_2C22():
        OP_8C(0x12, 135, 800)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2C22)

    NpcTalk(    #94
        0x12,
        "Researcher",
        "#5PWoosh!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x2)

    NpcTalk(    #95 op#A
        0x12,
        "Researcher",
        "#8A#11PZoooooom!\x02",
    )

    Sleep(200)

    def lambda_2C74():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2C74)

    def lambda_2C86():
        OP_8E(0xFE, 0x618, 0xFFFFFE0C, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C86)

    def lambda_2CA1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2CA1)

    def lambda_2CB3():
        OP_8F(0xFE, 0x7D0, 0xFFFFFE0C, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2CB3)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x11, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2CEF():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2CEF)

    ChrTalk(    #96
        0x106,
        "#055F#11PThe hell...?!\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #97
        0x106,
        (
            "#555F#11PWhat just happened there?\x02\x03",

            "She just up and ran off with Tita...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #98
        0x106,
        (
            "#057F#11PI hope I didn't just witness her getting abducted\x01",
            "by someone dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        "#792FYou don't need to worry about that.\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2E2D():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2E2D)

    def lambda_2E3B():
        OP_6D(2460, 0, 1800, 2400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2E3B)

    def lambda_2E53():
        OP_6C(322000, 2400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2E53)
    WaitChrThread(0x19, 0x0)

    ChrTalk(    #100
        0x106,
        "#052F#4POh. 'Sup, Kilika?\x02",
    )

    CloseMessageWindow()

    def lambda_2E87():
        OP_8E(0xFE, 0xE4C, 0x0, 0xFFFFFBDC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2E87)
    WaitChrThread(0x106, 0x1)
    TurnDirection(0x106, 0x10, 500)
    Sleep(300)

    ChrTalk(    #101
        0x10,
        "#791F#11PHer name is Erika Russell. She's Tita's mother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x106,
        (
            "#052F#6PHer mother?\x02\x03",

            "#40WTHAT is Tita's mother?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #103
        0x106,
        "#055F#4S#6PYou've gotta be KIDDING me!#2S\x02",
    )

    OP_7C(0x0, 0x190, 0xBB8, 0x96)
    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        (
            "#792F#11PHer parents came back here from abroad about\x01",
            "two weeks ago now. Erika and Dan Russell.\x02\x03",

            "Their arrival was somewhat unconventional,\x01",
            "admittedly...\x02\x03",

            "#791F...but they really are Tita's parents. I can assure\x01",
            "you of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x106,
        (
            "#555F#6PY-You're tryin' to tell me that woman is related\x01",
            "to her by blood...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 500)
    Sleep(300)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)

    ChrTalk(    #106
        0x10,
        (
            "#791F#11PAnd with that mystery solved, would you mind\x01",
            "if we got right to discussing work matters?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106)
    Sleep(200)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x106, 0, 600)
    Sleep(300)

    ChrTalk(    #107
        0x106,
        (
            "#052F#6PO-Oh... Yeah. Lay it on me.\x02\x03",

            "#051FI'm free until this evening, so if you've got any\x01",
            "quick jobs that need doing, I can knock' em out\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        (
            "#792F#11PWell, first, there's this one from the central\x01",
            "factory...\x02\x03",

            "They're requesting assistance with a variety of\x01",
            "tests for a prototype of a new weapon called the\x01",
            "'Orbal Gear.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        (
            "#052F#6POrbal...Gear?\x02\x03",

            "#555FHold up a minute. That sounds familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10,
        (
            "#791F#11PThe guild has officially accepted the request\x01",
            "that Erika mentioned to you earlier.\x02\x03",

            "It has your name on it, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x106,
        (
            "#552F#6PUgh... I can't believe this...\x02\x03",

            "She actually submitted that as an official\x01",
            "request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        (
            "#792F#11PI don't know much more about this Orbal Gear\x01",
            "than you do, I'm afraid.\x02\x03",

            "She merely described it as a weapon that\x01",
            "combines the finest in Liberl's orbal technology.\x02\x03",

            "It's being developed by the entire Russell family\x01",
            "together, to boot.\x02\x03",

            "#790FThe location you'll need to go is Zeiss Central\x01",
            "Factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x106,
        "#052F#6P...A new weapon?\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #114
        0x106,
        (
            "#053F#6PWait a sec. You said the whole Russell family,\x01",
            "right? Not just the adults?\x02\x03",

            "#057FPlease tell me Tita isn't involved in this crap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        (
            "#792F#11PI couldn't tell you. She didn't say.\x02\x03",

            "#791FI've heard Tita was about ready to graduate from \x01",
            "being an apprentice and become a full-fledged\x01",
            "engineer, though, so perhaps she is.\x02\x03",

            "Would her involvement be a problem to you, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x106,
        (
            "#552F#6PWell, no, but...\x02\x03",

            "#551F(I've never met her parents. I've only heard\x01",
            "about them from Tita, so it's not like I could\x01",
            "pretend to know what they're like.)\x02\x03",

            "(But her mom's nothing like she made her\x01",
            "sound...and she seems kinda...messed up in\x01",
            "the head.)\x02\x03",

            "...\x02\x03",

            "#057F(If that kook's got Tita involved in developing\x01",
            "some kinda new weapon...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #117
        0x106,
        "#050F#6PPut that request on hold for now, Kilika.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x10,
        (
            "#790F#11POn hold? Don't give it to anyone else for now,\x01",
            "I assume you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x106,
        (
            "#053F#6PYeah.\x02\x03",

            "#057FI'm gonna go and find out what's going on. \x01",
            "Don't even think of giving that to anyone\x01",
            "else before I'm back!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x106, 0x3, 0x0, 0x10)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x106, 0x3)
    OP_A2(0x2F85)
    OP_C2(0x1, 0x1F)
    OP_41(0x5, 0x0, 0xFF)
    OP_31(0x5, 0x10, 0x5A)
    OP_31(0x5, 0x5, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_35(0x5, 0xFFFF)
    OP_34(0x5, 0xFFFF)
    OP_35(0x5, 0x0)
    OP_BB(0x5, 0x6, 0x101)
    OP_37(0x5, 0x7F, 0x0)
    OP_37(0x5, 0x7F, 0x2)
    OP_41(0x5, 0x3E8, 0xFF)
    OP_34(0x5, 0x82)
    OP_34(0x5, 0x83)
    OP_34(0x5, 0x57)
    OP_34(0x5, 0x1E)
    OP_34(0x5, 0xA)
    NewScene("ED6_DT21/T3100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_15_28AC end

    def Function_16_39D2(): pass

    label("Function_16_39D2")

    OP_8C(0x106, 180, 600)

    def lambda_39DF():
        OP_8E(0xFE, 0x6CC, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_39DF)
    Sleep(1300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_16_39D2 end

    def Function_17_3A0E(): pass

    label("Function_17_3A0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3AD2")

    ChrTalk(    #120
        0x106,
        (
            "#057FMuch as I'd like to work on some of these, I need\x01",
            "to go and see what Tita's gotten herself wrapped\x01",
            "up in first.\x02\x03",

            "I've gotta get myself over to the central factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B95")

    label("loc_3AD2")


    ChrTalk(    #121
        0x106,
        (
            "#555FDamn. There sure are a lot of requests up here.\x02\x03",

            "#053FNone of them seem real urgent, at least. I can\x01",
            "afford to leave 'em for now.\x02\x03",

            "I've gotta get myself over to the central factory.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3B95")

    TalkEnd(0xFF)

    label("loc_3B98")

    Return()

    # Function_17_3A0E end

    SaveToFile()

Try(main)
