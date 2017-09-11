from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0700   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0700.x',
        MapIndex            = 9,
        MapDefaultBGM       = "ed60010",
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
        'Skip',                                 # 9
        'Fabree',                               # 10
        'Scherazard',                           # 11
        'Cassius',                              # 12
        'Alan',                                 # 13
        'Orvid',                                # 14
        'Target Camera',                        # 15
        'Downtown Rolent',                      # 16
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 9,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 9,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01450 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH02000 ._CH',             # 02
        'ED6_DT07/CH01290 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01450P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH02000P._CP',             # 02
        'ED6_DT07/CH01290P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
    )

    DeclNpc(
        X                   = 45064,
        Z                   = 4200,
        Y                   = 30855,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 31837,
        Z                   = 0,
        Y                   = 51534,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 43018,
        Z                   = 4000,
        Y                   = 33475,
        Direction           = 205,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 42909,
        Z                   = 4000,
        Y                   = 30908,
        Direction           = 282,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 36095,
        Z                   = 0,
        Y                   = 35619,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 38020,
        Z                   = 0,
        Y                   = 28750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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

    DeclNpc(
        X                   = 35320,
        Z                   = 0,
        Y                   = -13920,
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
        TriggerX            = 38000,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = 38000,
        ActorZ              = 2200,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 4000,
        TriggerY            = 41300,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 5500,
        ActorY              = 41800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34500,
        TriggerZ            = 0,
        TriggerY            = 46570,
        TriggerRange        = 800,
        ActorX              = 35000,
        ActorZ              = 1500,
        ActorY              = 46570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36142,
        TriggerZ            = 0,
        TriggerY            = 34342,
        TriggerRange        = 1000,
        ActorX              = 36095,
        ActorZ              = 1500,
        ActorY              = 35619,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A6",          # 00, 0
        "Function_1_390",          # 01, 1
        "Function_2_41D",          # 02, 2
        "Function_3_433",          # 03, 3
        "Function_4_457",          # 04, 4
        "Function_5_506",          # 05, 5
        "Function_6_5A4",          # 06, 6
        "Function_7_621",          # 07, 7
        "Function_8_154D",         # 08, 8
        "Function_9_1DBF",         # 09, 9
        "Function_10_1DC4",        # 0A, 10
        "Function_11_3C31",        # 0B, 11
        "Function_12_4F68",        # 0C, 12
        "Function_13_4F7D",        # 0D, 13
        "Function_14_4F92",        # 0E, 14
        "Function_15_4FCD",        # 0F, 15
        "Function_16_5011",        # 10, 16
        "Function_17_5060",        # 11, 17
        "Function_18_6736",        # 12, 18
    )


    def Function_0_2A6(): pass

    label("Function_0_2A6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2B2"),
        (SWITCH_DEFAULT, "loc_354"),
    )


    label("loc_2B2")

    ClearMapFlags(0x1)
    OP_B1("t0700_0")
    OP_6D(55210, -3070, 40180, 0)
    OP_6B(5870, 0)
    OP_6C(201000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x101, 41736, 4000, 31654, 118)
    SetChrPos(0x102, 41716, 4000, 32539, 129)
    SetChrPos(0xA, 43018, 4000, 33475, 205)
    SetChrPos(0xB, 42909, 4000, 30908, 282)
    ClearMapFlags(0x10)
    FadeToBright(2000, 0)
    Event(0, 11)
    Jump("loc_354")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36B")
    SetChrFlags(0xD, 0x80)
    Jump("loc_38F")

    label("loc_36B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_37D")
    SetChrFlags(0xD, 0x10)
    Jump("loc_38F")

    label("loc_37D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_38F")
    ClearChrFlags(0xD, 0x10)
    Jump("loc_38F")

    label("loc_38F")

    Return()

    # Function_0_2A6 end

    def Function_1_390(): pass

    label("Function_1_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B7")
    OP_B1("t0700_1")
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0xD, 0x4)
    Jump("loc_3F6")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DE")
    OP_B1("t0700_y")
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    Jump("loc_3F6")

    label("loc_3DE")

    OP_B1("t0700_0")
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)

    label("loc_3F6")

    OP_16(0x2, 0xFA0, 0xFFFE98A0, 0xFFFE8518, 0x30007)
    OP_71(0xE, 0x4)
    OP_71(0xE, 0x2)
    OP_72(0xE, 0x400)
    OP_72(0xE, 0x40)
    Return()

    # Function_1_390 end

    def Function_2_41D(): pass

    label("Function_2_41D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_432")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_41D")

    label("loc_432")

    Return()

    # Function_2_41D end

    def Function_3_433(): pass

    label("Function_3_433")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_456")
    OP_8D(0xFE, 29021, 54795, 33637, 48557, 4000)
    Jump("Function_3_433")

    label("loc_456")

    Return()

    # Function_3_433 end

    def Function_4_457(): pass

    label("Function_4_457")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05Rolent Landing Port\x01",
            "⇒　Grancel City\x01",
            "⇒　Bose City\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #1
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_457 end

    def Function_5_506(): pass

    label("Function_5_506")


    ChrTalk(    #2
        0x102,
        (
            "#010FThis is the entrance to the traffic\x01",
            "control tower.\x02\x03",

            "#010FIt looks like this is where they control the\x01",
            "lighting devices and the boarding bridge.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_5_506 end

    def Function_6_5A4(): pass

    label("Function_6_5A4")


    ChrTalk(    #3
        0x102,
        (
            "#010FIt looks like only employees are\x01",
            "allowed in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#509FWhen I'm told I can't go in,\x01",
            "I want to go in even more!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_6_5A4 end

    def Function_7_621(): pass

    label("Function_7_621")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_6BC")

    ChrTalk(    #5
        0xFE,
        (
            "It looks like the airliner that left\x01",
            "Bose has gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I'm getting worried. We haven't received\x01",
            "any contact from the airliner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1549")

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_7F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_789")
    OP_A2(0x5)

    ChrTalk(    #7
        0x8,
        (
            "The airliner's late...\x01",
            "I wonder what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "The airliner which should be coming\x01",
            "from Bose still hasn't arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "We're prepared to receive the\x01",
            "incoming ship, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F6")

    label("loc_789")


    ChrTalk(    #10
        0x8,
        (
            "The airliner's late...\x01",
            "I wonder what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "I'm positive it couldn't have been\x01",
            "an accident...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F6")

    Jump("loc_1549")

    label("loc_7F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_969")
    OP_A2(0x5)

    ChrTalk(    #12
        0x8,
        (
            "Have you heard of the high speed\x01",
            "cruiser, Arseille, that's used by\x01",
            "the Royal Family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "With a hull covered in elegant lines\x01",
            "and painted a pure white, it's certainly\x01",
            "fitting for those of royalty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "In addition, it boasts the best engine that orbal\x01",
            "technology can offer, and it's said to have the\x01",
            "highest performance output in the world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A46")

    label("loc_969")


    ChrTalk(    #15
        0x8,
        (
            "Have you heard of the high speed\x01",
            "cruiser, Arseille, that's used by\x01",
            "the Royal Family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "It boasts the best engine that orbal technology\x01",
            "can offer, and it's said to have the highest\x01",
            "performance output in the world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A46")

    Jump("loc_1549")

    label("loc_A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD2")
    OP_A2(0x5)

    ChrTalk(    #17
        0x8,
        (
            "This is the westward circling airliner,\x01",
            "Cecilia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "It's just about ready to leave for\x01",
            "Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "Thus far, no domestic airliner has\x01",
            "ever been involved in a big accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "The Liberl Orbalship Corporation has\x01",
            "paid particularly close attention to\x01",
            "safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "The fact that none of these airliners\x01",
            "have ever been in an accident is\x01",
            "something we're very proud of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C38")

    label("loc_BD2")


    ChrTalk(    #22
        0x8,
        (
            "All right, the orbal engine and\x01",
            "fuselage checks are complete!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "You can take off at any time!\x02",
    )

    CloseMessageWindow()

    label("loc_C38")

    Jump("loc_1549")

    label("loc_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A")
    OP_A2(0x5)

    ChrTalk(    #24
        0x8,
        (
            "The airliners have powerful orbal\x01",
            "engines mounted on-board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "I've been told that it costs untold\x01",
            "amounts of mira to develop\x01",
            "something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "It's only through the capital investment\x01",
            "from the Royal Family that these airliners\x01",
            "have become a reality.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_D5A")


    ChrTalk(    #27
        0x8,
        (
            "I've been told that it costs obscene\x01",
            "amounts of mira to develop an orbal\x01",
            "engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "It's only through the capital investment\x01",
            "from the Royal Family that these airliners\x01",
            "have become a reality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E20")

    Jump("loc_1549")

    label("loc_E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_E9E")

    ChrTalk(    #29
        0x8,
        "Whew, this job here is done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "The wind sure is calm today.\x01",
            "A perfect day for air travel, if\x01",
            "you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1549")

    label("loc_E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_120B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1153")
    OP_A2(0x5)

    ChrTalk(    #31
        0x8,
        (
            "Each of the five major cities in\x01",
            "Liberl is characteristically\x01",
            "different from the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "For starters, this is the scenic\x01",
            "regional city of Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "To the west lies Bose, the city of\x01",
            "commerce, which does a lot of\x01",
            "brisk business with the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "And farther west still lies the seaport\x01",
            "city of Ruan, which is Liberl's doorway\x01",
            "to the great waters beyond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "To the south lies the industrial city\x01",
            "of Zeiss, famous for orbment research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "And finally, resting on the east shore\x01",
            "of Valleria Lake is the beautiful royal\x01",
            "city of Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "Since each city is pretty distinct, it\x01",
            "might be interesting for you to visit\x01",
            "them all using an airliner sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1208")

    label("loc_1153")


    ChrTalk(    #38
        0x8,
        (
            "Since each of the five major cities is pretty\x01",
            "distinct, it might be interesting for you to\x01",
            "visit them one by one someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "I highly recommend using an\x01",
            "airliner for travel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1208")

    Jump("loc_1549")

    label("loc_120B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1386")
    OP_A2(0x5)

    ChrTalk(    #40
        0x8,
        (
            "There are two airliners which travel to the\x01",
            "five major cities: an eastward circling one\x01",
            "and westward circling one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "The westward circling airliner travels\x01",
            "from Grancel to Rolent, Bose, Ruan,\x01",
            "and Zeiss in that order...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "The eastward circling airliner travels in the\x01",
            "opposite direction from Grancel to Zeiss,\x01",
            "Ruan, Bose, and Rolent in that order.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1484")

    label("loc_1386")


    ChrTalk(    #43
        0x8,
        (
            "But just to let you know, there are\x01",
            "no routes connecting regions which\x01",
            "are not next to one another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "Any aircraft deviating from these set routes\x01",
            "either belongs to the Royal Army, the Royal Family\x01",
            "...or is flying in Liberl's airspace illegally.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1484")

    Jump("loc_1549")

    label("loc_1487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1509")
    OP_A2(0x5)

    ChrTalk(    #45
        0x8,
        (
            "The scheduled flight from Grancel\x01",
            "is about to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "I'd better start making landing guide\x01",
            "preparations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1549")

    label("loc_1509")


    ChrTalk(    #47
        0x8,
        (
            "The next flight will be arriving from\x01",
            "Bose this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1549")

    TalkEnd(0x8)
    Return()

    # Function_7_621 end

    def Function_8_154D(): pass

    label("Function_8_154D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_15F7")

    ChrTalk(    #48
        0xFE,
        (
            "One of the Liberl Orbalship Corporation's\x01",
            "airliners completely vanishing is\x01",
            "unprecedented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I hope both the airliner and its\x01",
            "passengers are safe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_15F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1672")

    ChrTalk(    #50
        0x9,
        "Just what is going on...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "With the airliner this late,\x01",
            "I can't help but think that\x01",
            "something happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E0")
    OP_A2(0x6)

    ChrTalk(    #52
        0x9,
        (
            "After the airliners were developed,\x01",
            "a lot of people started coming to\x01",
            "visit Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "Before that it was mostly merchants\x01",
            "who came to buy septium, lumber,\x01",
            "and vegetables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "I even hear that the number of\x01",
            "people traveling the roads on\x01",
            "foot has decreased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "You don't get tired riding on an airliner,\x01",
            "the reason being: they're fast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1886")

    label("loc_17E0")


    ChrTalk(    #56
        0x9,
        (
            "I even hear that the number of\x01",
            "people traveling the roads on\x01",
            "foot has decreased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "You don't get tired riding on an airliner,\x01",
            "the reason being: they're fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1886")

    Jump("loc_1DBB")

    label("loc_1889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1985")
    OP_A2(0x6)

    ChrTalk(    #58
        0x9,
        (
            "I know others may not be of\x01",
            "the same opinion, but is there\x01",
            "a smell that you just really like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "I just adore the sizzling smell\x01",
            "particular to hot airliner engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "I also love the smell of wet runways\x01",
            "on rainy days...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A19")

    label("loc_1985")


    ChrTalk(    #61
        0x9,
        (
            "I simply can't get enough of the\x01",
            "sizzling smell particular to hot\x01",
            "airliner engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "I also love the smell of wet runways\x01",
            "on rainy days...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A19")

    Jump("loc_1DBB")

    label("loc_1A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1AC2")

    ChrTalk(    #63
        0x9,
        (
            "Our biggest freight export is,\x01",
            "of course, septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "Since the orbment industry developed,\x01",
            "it looks like the mine has been seeing\x01",
            "a boom in demand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1B51")

    ChrTalk(    #65
        0x9,
        (
            "Your father was on that airliner\x01",
            "that just left, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "Is he off on business again?\x01",
            "That guy is seriously one\x01",
            "busy man...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1BED")

    ChrTalk(    #67
        0x9,
        (
            "All flights for today have finished,\x01",
            "but I still need to run a safety\x01",
            "inspection for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "'Be prepared'!\x01",
            "That's one of our mottos.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1CEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C84")
    OP_A2(0x6)

    ChrTalk(    #69
        0x9,
        "I am proud of the work I do here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "That's because I've always wanted\x01",
            "to work on orbal engines ever since\x01",
            "I can remember.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEB")

    label("loc_1C84")


    ChrTalk(    #71
        0x9,
        (
            "Right now I work in maintenance,\x01",
            "but in the future, my dream is to\x01",
            "be involved in airship design.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEB")

    Jump("loc_1DBB")

    label("loc_1CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D60")
    OP_A2(0x6)

    ChrTalk(    #72
        0x9,
        "Shoot! Today of all days I slept in...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "I must have had one too many\x01",
            "cold ones last night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1D60")


    ChrTalk(    #74
        0x9,
        (
            "Okay, I'd better hurry up with\x01",
            "my pre-work inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        "It's time to get pumped!\x02",
    )

    CloseMessageWindow()

    label("loc_1DBB")

    TalkEnd(0x9)
    Return()

    # Function_8_154D end

    def Function_9_1DBF(): pass

    label("Function_9_1DBF")

    Call(0, 10)
    Return()

    # Function_9_1DBF end

    def Function_10_1DC4(): pass

    label("Function_10_1DC4")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1FD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F42")
    OP_A2(0x7)

    ChrTalk(    #76
        0xC,
        (
            "The Royal Army is out searching\x01",
            "for the missing airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xC,
        (
            "But according to company information,\x01",
            "it looks like it still hasn't been found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        (
            "Of all the things that could have happened...\x01",
            "Now I won't be able to check out the hot girls\x01",
            "coming and going on the airliners for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xC,
        (
            "Come on, Royal Army. This is what \x01",
            "I'm paying my taxes for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD6")

    label("loc_1F42")


    ChrTalk(    #80
        0xC,
        (
            "The Royal Army is out searching\x01",
            "for the missing airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xC,
        (
            "But according to company information,\x01",
            "it looks like it still hasn't been found.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD6")

    Jump("loc_3C2D")

    label("loc_1FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_END)), "loc_2BE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B32")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(35650, 0, 32590, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrPos(0x101, 35850, 0, 33370, 0)
    SetChrPos(0x102, 36660, 0, 32180, 0)
    SetChrPos(0x103, 35060, 0, 31950, 0)
    TurnDirection(0xC, 0x101, 0)
    OP_0D()

    ChrTalk(    #82
        0xC,
        "P-Please excuse the delay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        (
            "The airliner should be arriving any\x01",
            "time now, so please be patient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#004F#4PYo, Alan.\x01",
            "It's us if you haven't noticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xC,
        (
            "Oh, it's you guys. Ooh, and Scherazard, too!\x01",
            "(Thank you, Aidios, for this feast of the eyes!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xC,
        "So, uh, what's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#012F#4PYou didn't by chance happen to see\x01",
            "a girl in a school uniform around\x01",
            "here, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xC,
        "A girl in a school uniform?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xC,
        "A school uniform from where?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#002F#4PFrom the Jenis Royal Academy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xC,
        "Oh, baby! Those uniforms are so hot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xC,
        (
            "The contrast of those neatly pleated\x01",
            "white skirts and navy blue socks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xC,
        (
            "Oh, yes, I can see them now!\x01",
            "I totally forget what the boys'\x01",
            "uniforms look like though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#007F#4PThis is one obsession I just\x01",
            "don't get...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x103,
        (
            "#027FThus defineth man's eternal struggle...\x02\x03",

            "#027FBack on topic here, so you didn't see\x01",
            "a girl in a royal academy uniform?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        (
            "Nope, not this month.\x01",
            "And believe me, I watch for those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xC,
        (
            "I check all the passengers boarding\x01",
            "and disembarking, so I can tell you\x01",
            "at least that she hasn't come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x103,
        (
            "#022FWhich means that she came to\x01",
            "Rolent along the roads without\x01",
            "using an airliner...\x02\x03",

            "#022FThis complicates things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #99
        0x102,
        (
            "#012FOur search field suddenly got\x01",
            "much bigger.\x02\x03",

            "#012FCome to think of it, there must\x01",
            "be others, so they've got to be\x01",
            "hiding somewhere...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #100
        0x101,
        "#004FWait, that reminds me...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #101
        0x103,
        "#023FWhat does, Estelle?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Pull out Servais Leaf]\x01",      # 0
            "[When's dinner?!]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2748")
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #102
        "\x07\x05Estelle pulled out the Servais Leaf found in the attic.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #103
        0x101,
        (
            "#006FI almost forgot that we found this.\x01",
            "Could this be some sort of a clue?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2920")

    label("loc_2748")


    ChrTalk(    #104
        0x101,
        (
            "#008FWhen's din-... Er, what was\x01",
            "I saying again...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #105
        0x102,
        (
            "#018FHow about taking this a little more\x01",
            "seriously, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x103,
        (
            "#022FDid you notice something back\x01",
            "at the mayor's place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#001FThat's right! That's what I was\x01",
            "trying to say!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #108
        "\x07\x05Estelle pulled out the Servais Leaf found in the attic.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #109
        0x101,
        (
            "#006FI almost forgot that we found this.\x01",
            "Could this be some sort of a clue?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2920")


    ChrTalk(    #110
        0x102,
        (
            "#010FOh right... We did find that.\x02\x03",

            "#010FSchera, do you know of any places\x01",
            "nearby where Servais trees grow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x103,
        (
            "#026FServais trees, huh...?\x02\x03",

            "#020FI'm pretty certain they grow in\x01",
            "Mistwald, south of Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#010FMistwald... That's the forest in the\x01",
            "opposite direction from home as\x01",
            "Rolent, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#006FIt seems like it's worth looking into.\x02\x03",

            "#006FThat settles it. Let's hit up the highway\x01",
            "through Rolent's south gate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "You're really excited, aren't you?\x01",
            "Well, whatever it is, good luck.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x263)
    OP_28(0x1B, 0x1, 0x10)
    OP_28(0x1B, 0x1, 0x20)
    OP_28(0x1B, 0x1, 0x40)
    EventEnd(0x0)
    Jump("loc_2BE5")

    label("loc_2B32")


    ChrTalk(    #115
        0xC,
        (
            "The Jenis Royal Academy, huh...?\x01",
            "Those uniforms sure are hot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        (
            "The contrast of those neatly pleated\x01",
            "white skirts and navy blue socks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        "Oh, yes, I can see them now!\x02",
    )

    CloseMessageWindow()

    label("loc_2BE5")

    Jump("loc_3C2D")

    label("loc_2BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_2D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD4")
    OP_A2(0x7)

    ChrTalk(    #118
        0xC,
        (
            "The airliner coming from Bose\x01",
            "is late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xC,
        (
            "Thanks to that there's no eye candy\x01",
            "for me to watch disembark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        (
            "This puts a serious cramp in\x01",
            "my one sole pastime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x103,
        "#025FHonestly, this guy never changes...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D46")

    label("loc_2CD4")


    ChrTalk(    #122
        0xC,
        (
            "The airliner coming from Bose\x01",
            "is late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xC,
        (
            "Thanks to that there's no eye candy\x01",
            "for me to watch disembark.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D46")

    Jump("loc_3C2D")

    label("loc_2D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3060")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FAD")
    OP_A2(0x7)

    ChrTalk(    #124
        0xC,
        (
            "Recently, it seems that there are some\x01",
            "sky bandits using an airship to pull off\x01",
            "robberies in the Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xC,
        (
            "I'm gonna have to be more strict\x01",
            "with passenger checks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xC,
        (
            "If a criminal managed to get on-board\x01",
            "who knows what might happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#004FWell I'll be. Alan, you actually\x01",
            "sounded responsible for a second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xC,
        (
            "Well, that's because I'd never forgive\x01",
            "myself if I allowed some hotties to\x01",
            "get in harm's way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xC,
        (
            "Not to mention, it gives me a reason to\x01",
            "check out the chicks more closely, too.\x01",
            "That's two birds with one stone, baby!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#007FI was a fool for admiring you...\x02",
    )

    CloseMessageWindow()
    Jump("loc_305D")

    label("loc_2FAD")


    ChrTalk(    #131
        0xC,
        (
            "Recently, it seems that there are some\x01",
            "sky bandits using an airship to pull off\x01",
            "robberies in the Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xC,
        (
            "I'm gonna have to be more strict\x01",
            "with passenger checks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305D")

    Jump("loc_3C2D")

    label("loc_3060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_32D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_320F")
    OP_A2(0x7)

    ChrTalk(    #133
        0xC,
        (
            "Before and after the queen's birthday\x01",
            "celebration is when the airliners are\x01",
            "the most crowded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xC,
        (
            "Now if I just had a girlfriend,\x01",
            "I could take her to see the\x01",
            "sights in the Royal City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        (
            "What I wouldn't give to see our queen,\x01",
            "who never gave in to the powerful emperor\x01",
            "and the opposing minister, just once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xC,
        (
            "And of course, I mustn't forget her\x01",
            "granddaughter, Princess Klaudia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xC,
        "Heh heh heh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_32CF")

    label("loc_320F")


    ChrTalk(    #138
        0xC,
        (
            "Before and after the queen's birthday\x01",
            "celebration is when the airliners are\x01",
            "the most crowded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xC,
        (
            "Now if I just had a girlfriend,\x01",
            "I could take her to see the\x01",
            "sights in the Royal City...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32CF")

    Jump("loc_3C2D")

    label("loc_32D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_34C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340B")
    OP_A2(0x7)

    ChrTalk(    #140
        0xC,
        (
            "Homegrown girls are fine, but those chicks\x01",
            "coming from the Royal City and Bose have\x01",
            "that extra layer of polished beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xC,
        (
            "Speaking of the Royal City, Queen\x01",
            "Alicia's granddaughter, Princess\x01",
            "Klaudia, lives there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xC,
        (
            "Rumor has it that she's quite the\x01",
            "looker. I wonder if it's true...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C4")

    label("loc_340B")


    ChrTalk(    #143
        0xC,
        (
            "Those chicks coming from the\x01",
            "Royal City and Bose have that\x01",
            "extra layer of polished beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xC,
        (
            "But even giving up the homegrown\x01",
            "girls for one of them would be a\x01",
            "difficult choice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C4")

    Jump("loc_3C2D")

    label("loc_34C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3544")

    ChrTalk(    #145
        0xC,
        (
            "Heh heh heh...we're making a good\x01",
            "start today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xC,
        (
            "For now, I'd probably rate that\x01",
            "girl an 83.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#501F???\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C2D")

    label("loc_3544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_36E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3647")
    OP_A2(0x7)

    ChrTalk(    #148
        0xC,
        "How utterly disappointing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xC,
        (
            "There wasn't a single chick who\x01",
            "was my type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xC,
        (
            "There was a chick on the flight from Bose\x01",
            "yesterday. She had a strange accent, but\x01",
            "she was quite the looker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xC,
        "I wonder if she's still in Rolent.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_3647")


    ChrTalk(    #152
        0xC,
        (
            "There was a chick on the flight from Bose\x01",
            "yesterday. She had a strange accent, but\x01",
            "she was quite the looker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xC,
        "I wonder if she's still in Rolent.\x02",
    )

    CloseMessageWindow()

    label("loc_36E1")

    Jump("loc_3C2D")

    label("loc_36E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_3971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E6")
    OP_A2(0x7)

    ChrTalk(    #154
        0xC,
        (
            "Luscious chocolate skin,\x01",
            "captivating ruby eyes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xC,
        (
            "Scherazard's quite the exotic beauty,\x01",
            "wouldn't you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xC,
        (
            "She's got that fascinating charm\x01",
            "that people in Liberl don't have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#007FAlan's off in his little world again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x102,
        "#010FHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xC,
        (
            "I've actually gone drinking with\x01",
            "Scherazard before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xC,
        (
            "But the strange thing is, I have\x01",
            "absolutely no memory of that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xC,
        (
            "Ha ha ha, maybe I should try\x01",
            "and ask her out again?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(500)
    Jump("loc_396E")

    label("loc_38E6")


    ChrTalk(    #162
        0xC,
        (
            "There were no cute girls on\x01",
            "the flight this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xC,
        (
            "I guess all I can do now is look forward\x01",
            "to the flight this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396E")

    Jump("loc_3C2D")

    label("loc_3971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF2")
    OP_A2(0x7)

    ChrTalk(    #164
        0xC,
        (
            "A lot of people will leave from\x01",
            "Rolent today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xC,
        "And a lot of people will come...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xC,
        (
            "Which means a lot of chicks\x01",
            "will pass through here.\x01",
            "Score!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xC,
        (
            "Staring at these girls is one\x01",
            "of my simple pleasures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xC,
        (
            "You know what I mean, right,\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #169
        0x102,
        "#010FUh, sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#007FAlan, you never change a bit.\x02\x03",

            "#501FAll this nonsense is the reason\x01",
            "why you can't get a girlfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xC,
        "You wound me, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xC,
        (
            "But it's because of this enjoyment that\x01",
            "I feel that it's worth doing this job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xC,
        (
            "It's a paradise!\x01",
            "Ha ha ha ha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#007FThis guy's a serious nutjob...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C2D")

    label("loc_3BF2")


    ChrTalk(    #175
        0xC,
        (
            "Staring at these girls is one\x01",
            "of my simple pleasures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2D")

    TalkEnd(0xC)
    Return()

    # Function_10_1DC4 end

    def Function_11_3C31(): pass

    label("Function_11_3C31")

    OP_1D(0x58)
    OP_71(0xA, 0x4)
    OP_71(0xA, 0x2)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0xD, 0x4)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    EventBegin(0x0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_43(0x101, 0x0, 0x0, 0xC)
    OP_43(0x102, 0x0, 0x0, 0xD)
    OP_43(0xA, 0x0, 0x0, 0xF)
    OP_43(0xB, 0x0, 0x0, 0xE)
    OP_43(0xB, 0x1, 0x0, 0x10)
    OP_67(0, 4500, -10000, 0)
    OP_6B(6000, 0)

    def lambda_3CAF():
        OP_67(0, 9500, -10000, 14000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3CAF)

    def lambda_3CC7():
        OP_6B(2800, 14000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_3CC7)
    OP_22(0x75, 0x0, 0x64)
    OP_A2(0x4)
    OP_6D(42820, 4000, 32330, 14000)
    OP_A5(0x4)
    Sleep(1000)

    ChrTalk(    #176
        0xB,
        (
            "#080FWell, it looks like it's time for\x01",
            "me to board my flight.\x02\x03",

            "#080FEstelle, don't do anything I wouldn't\x01",
            "do myself and try not to be a handful\x01",
            "for Joshua either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#007F#3PFor the umpteenth time,\x01",
            "I heard you already.\x02\x03",

            "#000FHow about you try not to go overboard\x01",
            "yourself with your own work? You're\x01",
            "not getting any younger, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xB,
        (
            "#085FSay what you will, but I'm not\x01",
            "about to be overtaken by any\x01",
            "youngsters.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(    #179
        0xB,
        (
            "#080FScherazard, I'm really sorry about\x01",
            "placing all this work on your\x01",
            "shoulders at the last minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xA,
        (
            "#027FPlease, don't be.\x02\x03",

            "#027FI am slightly concerned, however,\x01",
            "about whether or not I can do a\x01",
            "decent job in your place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xB,
        (
            "#080FThere's no need to be humble,\x01",
            "Silver Streak.\x02\x03",

            "#080FAnd I don't mean to make your\x01",
            "life any more difficult, but please\x01",
            "keep an eye on these two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xA,
        (
            "#021FYou just leave that to me.\x02\x03",

            "#021FIs tightening up the reins and not\x01",
            "spoiling these two fine with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xB,
        (
            "#081FYou definitely understand the\x01",
            "way I think.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x101,
        "#009F#3PWhat's this all about...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        (
            "#019F#3PHa ha, it looks to me like a mutual\x01",
            "understanding between master and\x01",
            "pupil.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #186
        (
            "\x07\x05The Grancel-bound airliner, Linde,\x01",
            "will be departing shortly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #187
        (
            "All passengers, please board the\x01",
            "airship now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0xB, 0, 400)
    OP_8C(0xB, 45, 400)

    ChrTalk(    #188
        0xB,
        "#084FUh-oh, I'd better take my seat.\x02",
    )

    CloseMessageWindow()

    def lambda_4240():
        OP_67(0, 4370, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4240)

    def lambda_4258():
        OP_6E(365, 6000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_4258)
    OP_A2(0x4)
    OP_A2(0x2)
    OP_A2(0x3)
    OP_A5(0x2)
    OP_A5(0x4)
    OP_A3(0x3)
    Sleep(500)

    ChrTalk(    #189
        0x102,
        (
            "#010FHave a great trip, Dad.\x01",
            "We'll take care of everything\x01",
            "here while you're gone.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "[Hurry back!]\x01",                                    # 0
            "[Don't forget to bring me back a souvenir!]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4350"),
        (1, "loc_445E"),
        (SWITCH_DEFAULT, "loc_45AB"),
    )


    label("loc_4350")


    ChrTalk(    #190
        0x101,
        (
            "#006FWhen you're done with your work,\x01",
            "make sure you come straight home.\x01",
            "And no goofing off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xB,
        (
            "#083FIs that any way to see your\x01",
            "beloved papa off?\x02\x03",

            "#080FOh well...I'll try my best to come\x01",
            "home as soon as I can.\x02\x03",

            "#080FAll right, you two, be good\x01",
            "while I'm gone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45AB")

    label("loc_445E")


    ChrTalk(    #192
        0x101,
        (
            "#501FI'm not sure everywhere you'll be\x01",
            "going, but don't forget to bring me\x01",
            "back a souvenir!\x02\x03",

            "#001FA little fancy something would\x01",
            "be nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xB,
        (
            "#083FHey now! This trip is for business,\x01",
            "not pleasure.\x02\x03",

            "#080FIf I have any money left over,\x01",
            "I'll certainly think about it though.\x02\x03",

            "#080FAll right, you two, be good\x01",
            "while I'm gone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45AB")

    label("loc_45AB")

    Sleep(500)
    OP_8C(0x0, 90, 0)
    OP_8C(0x1, 90, 0)

    def lambda_45C4():
        OP_67(0, 7390, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_45C4)

    def lambda_45DC():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_45DC)
    OP_22(0x78, 0x0, 0x64)
    OP_70(0xD, 0x118)
    Sleep(3000)
    OP_6F(0xB, 2)
    OP_70(0xB, 0x118)
    Sleep(700)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0xB)
    WaitChrThread(0x1, 0x3)
    Fade(1500)
    OP_6D(54360, -3070, 41690, 0)
    OP_67(0, 40540, -45000, 0)
    OP_6B(740, 0)
    OP_6C(208000, 0)
    OP_6E(510, 0)
    OP_8C(0x0, 45, 0)
    OP_8C(0x1, 45, 0)
    OP_8C(0xA, 45, 0)
    SetChrFlags(0xB, 0x80)

    def lambda_4679():
        OP_6C(223000, 13000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_4679)
    LoadEffect(0x0, "map\\\\mp028_00.eff")
    Play3DEffect(0x0, 0x0, 0xB, "Frame1_E0000_ground_Layer1", 0xFFFFE7C8, 0x8FC, 0x2567, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Play3DEffect(0x0, 0x1, 0xB, "Frame1_E0000_ground_Layer1", 0x1838, 0x8FC, 0x2567, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xB, 200)
    OP_6F(0xC, 200)
    OP_70(0xB, 0x221)
    OP_70(0xC, 0x221)
    OP_73(0xB)

    def lambda_4743():
        OP_6D(54360, 1000, 41690, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4743)
    OP_6F(0xB, 546)
    OP_6F(0xC, 546)
    OP_70(0xB, 0x320)
    OP_70(0xC, 0x320)
    OP_73(0xB)

    def lambda_477A():
        OP_67(0, 39850, -45000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_477A)

    def lambda_4792():
        OP_6C(314000, 12000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_4792)
    OP_6F(0xB, 800)
    OP_6F(0xC, 800)
    OP_70(0xB, 0x384)
    OP_70(0xC, 0x384)
    OP_73(0xB)
    OP_B0(0xB, 0x28)
    OP_B0(0xC, 0x28)
    OP_6F(0xB, 901)
    OP_6F(0xC, 901)
    OP_70(0xB, 0x3B6)
    OP_70(0xC, 0x3B6)
    OP_73(0xB)
    OP_B0(0xB, 0x32)
    OP_B0(0xC, 0x32)
    OP_6F(0xB, 951)
    OP_6F(0xC, 951)
    OP_70(0xB, 0x3E8)
    OP_70(0xC, 0x3E8)
    OP_73(0xB)
    OP_B0(0xB, 0x3C)
    OP_B0(0xC, 0x3C)
    OP_6F(0xB, 1001)
    OP_6F(0xC, 1001)
    OP_70(0xB, 0x41A)
    OP_70(0xC, 0x41A)
    OP_73(0xB)
    OP_B0(0xB, 0x46)
    OP_B0(0xC, 0x46)
    OP_6F(0xB, 1051)
    OP_6F(0xC, 1051)
    OP_70(0xB, 0x44C)
    OP_70(0xC, 0x44C)
    OP_73(0xB)
    OP_B0(0xB, 0x50)
    OP_B0(0xC, 0x50)
    OP_6F(0xB, 1101)
    OP_6F(0xC, 1101)
    OP_70(0xB, 0x47E)
    OP_70(0xC, 0x47E)
    OP_73(0xB)
    OP_B0(0xB, 0x5A)
    OP_B0(0xC, 0x5A)
    OP_6F(0xB, 1151)
    OP_6F(0xC, 1151)
    OP_70(0xB, 0x4B0)
    OP_70(0xC, 0x4B0)
    OP_73(0xB)
    OP_B0(0xB, 0x64)
    OP_B0(0xC, 0x64)
    OP_6F(0xB, 1201)
    OP_6F(0xC, 1201)
    OP_70(0xB, 0x4E2)
    OP_70(0xC, 0x4E2)
    OP_73(0xB)
    OP_B0(0xB, 0x6E)
    OP_B0(0xC, 0x6E)
    OP_6F(0xB, 1251)
    OP_6F(0xC, 1251)
    OP_70(0xB, 0x514)
    OP_70(0xC, 0x514)
    OP_73(0xB)
    OP_B0(0xB, 0x78)
    OP_B0(0xC, 0x78)
    OP_6F(0xB, 1301)
    OP_6F(0xC, 1301)
    OP_70(0xB, 0x546)
    OP_70(0xC, 0x546)
    OP_73(0xB)
    OP_B0(0xB, 0x82)
    OP_B0(0xC, 0x82)
    OP_6F(0xB, 1351)
    OP_6F(0xC, 1351)
    OP_70(0xB, 0x578)
    OP_70(0xC, 0x578)
    OP_73(0xB)
    OP_B0(0xB, 0x96)
    OP_B0(0xC, 0x96)
    OP_6F(0xB, 1401)
    OP_6F(0xC, 1401)
    OP_70(0xB, 0x7D0)
    OP_70(0xC, 0x7D0)
    FadeToDark(2000, 0, -1)
    Sleep(1500)
    OP_24(0x75, 0x5A)
    OP_24(0x77, 0x5A)
    Sleep(100)
    OP_24(0x75, 0x50)
    OP_24(0x77, 0x50)
    Sleep(100)
    OP_24(0x75, 0x46)
    OP_24(0x77, 0x46)
    Sleep(100)
    OP_24(0x75, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(100)
    OP_24(0x75, 0x32)
    OP_24(0x77, 0x32)
    Sleep(100)
    OP_24(0x75, 0x28)
    OP_24(0x77, 0x28)
    Sleep(100)
    OP_24(0x75, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(100)
    OP_24(0x75, 0x14)
    OP_24(0x77, 0x14)
    Sleep(100)
    OP_24(0x75, 0xA)
    OP_24(0x77, 0xA)
    Sleep(100)
    OP_23(0x75)
    OP_23(0x77)
    Sleep(1000)
    OP_0D()
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    SetChrPos(0x101, 41807, 4000, 39449, 170)
    SetChrPos(0x102, 42334, 4000, 37937, 315)
    SetChrPos(0xA, 40186, 4000, 39987, 158)
    OP_67(0, 8000, -10000, 0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_6D(41380, 5450, 39120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearChrFlags(0x8, 0x80)
    OP_72(0xA, 0x4)
    OP_72(0xA, 0x2)
    Sleep(1000)

    ChrTalk(    #194
        0x102,
        "#010FHe's gone...again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#003F#5P...Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xA,
        (
            "#020FCome on, you two. There's no need\x01",
            "to look so down. Your father will\x01",
            "be back in no time.\x02\x03",

            "#020FI don't know what kind of investigation he's been\x01",
            "asked to do this time, but when it comes to your\x01",
            "father, he'll have it done before you know it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #197
        0x101,
        (
            "#009F#5PI-I'm not sad that he's gone!\x02\x03",

            "#009FHe's always been away more\x01",
            "than he's been at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xA,
        (
            "#021FAll right, all right,\x01",
            "if you say so.\x02\x03",

            "#020FAnyway, I'm going to get to work on\x01",
            "those jobs your father left for me...\x02\x03",

            "#020FBut if you run into any trouble,\x01",
            "give me a holler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        (
            "#006F#5PWill do. But first, I'd like to try and\x01",
            "finish a few jobs with Joshua.\x02\x03",

            "#006FI want to see what we're capable\x01",
            "of doing as junior bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        (
            "#020FAll right.\x01",
            "If you insist.\x02\x03",

            "#020FI imagine that with Joshua tagging\x01",
            "along, there's probably not much\x01",
            "to be worried about.\x02\x03",

            "#020FGood luck, you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#006F#5PThanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        "#010FWe'll do our best.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A5(0x3)
    SetChrFlags(0xA, 0x80)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #203
        0x102,
        (
            "#010FSo, what do you want to do now,\x01",
            "Estelle?\x02\x03",

            "#010FShall we go stop by the guild?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #204
        0x101,
        (
            "#000F#5PYeah, we should probably talk to\x01",
            "Aina and find out what jobs are\x01",
            "waiting for us.\x02\x03",

            "#001FLet's GOOO!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_20(0x5DC)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    OP_A2(0x213)
    OP_21()
    OP_1E()
    Return()

    # Function_11_3C31 end

    def Function_12_4F68(): pass

    label("Function_12_4F68")

    OP_A6(0x0)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_12_4F68 end

    def Function_13_4F7D(): pass

    label("Function_13_4F7D")

    OP_A6(0x1)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_13_4F7D end

    def Function_14_4F92(): pass

    label("Function_14_4F92")

    OP_A6(0x2)
    OP_8E(0xFE, 0xB3BD, 0x1068, 0x7946, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xCF15, 0x1068, 0x7946, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    OP_A3(0x2)
    Return()

    # Function_14_4F92 end

    def Function_15_4FCD(): pass

    label("Function_15_4FCD")

    OP_A6(0x3)

    label("loc_4FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4FE2")
    TurnDirection(0xFE, 0xB, 0)
    OP_48()
    Jump("loc_4FD0")

    label("loc_4FE2")

    OP_A6(0x3)
    OP_8E(0xFE, 0x96E4, 0xFA0, 0x988D, 0x7D0, 0x0)
    OP_8E(0xFE, 0x81AC, 0x7D0, 0x988D, 0x7D0, 0x0)
    OP_A3(0x3)
    Return()

    # Function_15_4FCD end

    def Function_16_5011(): pass

    label("Function_16_5011")

    OP_A6(0x4)
    OP_6C(72000, 14000)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_6D(48784, 4000, 31814, 6000)
    OP_A3(0x4)
    OP_A6(0x4)
    OP_6D(55314, 1821, 30831, 4000)
    OP_6D(55314, 6821, 30831, 4000)
    OP_A3(0x4)
    Return()

    # Function_16_5011 end

    def Function_17_5060(): pass

    label("Function_17_5060")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_50FC")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #205
        0xFE,
        "Yes? Is there something else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "I'm busy preparing for some\x01",
            "business negotiations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "Would you mind leaving me alone?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    Jump("loc_6732")

    label("loc_50FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_516D")

    ChrTalk(    #208
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "I've got to succeed with my business\x01",
            "negotiations in Bose no matter what\x01",
            "it takes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6732")

    label("loc_516D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x384)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D39")
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x5, 0x1, 0x4)
    OP_A2(0x8)
    Fade(1000)
    EventBegin(0x0)
    SetChrPos(0x101, 38840, 0, 27320, 315)
    SetChrPos(0x102, 37840, 0, 26710, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51E4")
    SetChrPos(0x2, 38840, 0, 25820, 0)
    SetChrPos(0x3, 37840, 0, 25210, 0)

    label("loc_51E4")

    OP_6D(37930, 0, 27910, 0)
    OP_6C(135000, 0)
    OP_6B(2800, 0)
    OP_6E(280, 0)
    OP_4A(0xD, 255)
    OP_8C(0xD, 180, 0)
    OP_0D()

    ChrTalk(    #210
        0xFE,
        (
            "What's that, you say?\x01",
            "You've found the mushroom?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 0)

    ChrTalk(    #211
        0x101,
        "#002FYep. We found it, all right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #212
        0xFE,
        "Oh, wonderful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#505FBut it might be different than the\x01",
            "one we heard about from you.\x02\x03",

            "#505FYou see, this mushroom attracts\x01",
            "monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "Uh, well...it's like this...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(    #215
        0x102,
        (
            "#012FSo even though you knew the risk,\x01",
            "you hired us for the job, Orvid?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #216
        0xFE,
        (
            "Wh-What? H-How was I supposed to\x01",
            "know something like that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #217
        0xFE,
        (
            "And besides, a bracer's job is\x01",
            "to deal with danger, right?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)
    OP_94(0x1, 0x101, 0x0, 0x1F4, 0x1770, 0x0)

    ChrTalk(    #218
        0x101,
        (
            "#005FWell, a little heads up would have\x01",
            "been nice so we could have at least\x01",
            "been prepared!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0xD, 0x9470, 0x0, 0x70EE, 0x258, 0x2710)
    OP_96(0xD, 0x927C, 0x0, 0x731E, 0xC8, 0x2710)
    Sleep(400)

    ChrTalk(    #219
        0x102,
        (
            "#012FNever mind us, the big question\x01",
            "here is your motive.\x02\x03",

            "What do you intend to use\x01",
            "this mushroom for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#009FYeah, this thing could be a weapon.\x02\x03",

            "Fess up! You had some big,\x01",
            "nefarious plan in mind, right?!\x01",
            "A nefarious mushroom plan!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xD, 0x9484, 0x0, 0x704E, 0x7D0, 0x0)
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #221
        0xFE,
        (
            "Er...what?\x01",
            "Isn't it obvious what I'm\x01",
            "going to use it for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "For cooking of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        "#004FWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        "#014FCooking...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#004FAre you trying to tell me that\x01",
            "people actually eat this thing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)
    OP_62(0xD, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0xFE,
        (
            "This is why it's such a pain to\x01",
            "deal with country bumpkins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "In the hands of a skilled chef, the\x01",
            "more distinct the ingredient, the\x01",
            "more profound the taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "And from that perspective, the Firefly\x01",
            "Fungus is the king of them all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "This is, no doubt,\x01",
            "the ultimate ingredient!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_588D")
    OP_62(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_588D")

    Sleep(400)

    ChrTalk(    #230
        0x102,
        "#017F...\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(    #231
        0x101,
        (
            "#509FSo pretty much what you're saying is,\x01",
            "that it's for people with bizarre eating\x01",
            "habits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "Hmph! That's the talk of one\x01",
            "unacquainted with a true delicacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "But then again, commoners such as\x01",
            "yourselves would never have an\x01",
            "opportunity to try such dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x101,
        (
            "#007FAnd praise be to heaven for that...\x02\x03",

            "I'd never want to gnaw on a ratty\x01",
            "green mushroom like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x102,
        "#018F(Agreed. It looks pretty nasty...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "Anyway, I have other business\x01",
            "preparations to make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "Now if you don't mind, I'd ask that\x01",
            "you hand over the mushroom and leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        "#007FYeah, please take it.\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0xD, 0x1F4, 0x7D0, 0x0)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #239
        "\x07\x00Handed over \x07\x02Firefly Fungus\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x384, 1)
    OP_94(0x1, 0x101, 0xB4, 0x3E8, 0x7D0, 0x0)

    ChrTalk(    #240
        0xFE,
        (
            "On behalf of this mushroom, I shall\x01",
            "turn a blind eye to your ignorance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "And as promised, I will pay you,\x01",
            "so be grateful to your client.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        (
            "#009FNobody's going to buy that mushroom,\x01",
            "I hope you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #243
        0x101,
        "#009FCome on, Joshua! Let's go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x102,
        (
            "#017FPlease excuse us.\x01",
            "We will be going now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #245
        0xFE,
        "Yes, please do.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #246
        "\x07\x00Quest \x07\x02[Mushroom Hunt] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xD, 0x10)
    Fade(1000)
    OP_6B(3300, 0)
    OP_6E(262, 0)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    TalkEnd(0xD)
    Jump("loc_6732")

    label("loc_5D39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_6056")

    ChrTalk(    #247
        0xFE,
        "Is there still a problem?\x02",
    )

    CloseMessageWindow()

    label("loc_5D62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6049")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Mushroom characteristics]\x01",      # 0
            "[Never mind]\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5DCA"),
        (1, "loc_6001"),
        (SWITCH_DEFAULT, "loc_6001"),
    )


    label("loc_5DCA")


    ChrTalk(    #248
        0xFE,
        (
            "It is said that the Firefly Fungus only\x01",
            "grows in soil rich with septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "It seems that it normally grows in\x01",
            "areas with patches of grass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "However, since it is buried in the\x01",
            "dirt, if you don't look closely, you\x01",
            "won't find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "The only other characteristic I can\x01",
            "tell you is that, like its namesake,\x01",
            "it glows with a light green color.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        "I guess that's about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x101,
        (
            "#000FSo basically, all we need to do is find\x01",
            "a glowing mushroom in a patch of grass\x01",
            "along the Malga Trail, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "I ask that you find one as soon\x01",
            "as possible.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6046")

    label("loc_6001")


    ChrTalk(    #255
        0xFE,
        (
            "I ask that you find one as soon\x01",
            "as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_5F(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_6046")

    label("loc_6046")

    Jump("loc_5D62")

    label("loc_6049")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6732")

    label("loc_6056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_6732")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6664")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_624E")
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)

    ChrTalk(    #256
        0xFE,
        "Are you free?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "I have an urgent job, so do you have\x01",
            "some time to hear my request?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6241")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Listen]\x01",            # 0
            "[Don't listen]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_6131"),
        (1, "loc_616E"),
        (SWITCH_DEFAULT, "loc_623E"),
    )


    label("loc_6131")


    ChrTalk(    #258
        0x101,
        "#000FUh, sure. We've got some time.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Call(0, 18)
    Jump("loc_623E")

    label("loc_616E")


    ChrTalk(    #259
        0x101,
        (
            "#505FUm, I'm sorry...\x02\x03",

            "We're still a little busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "That's too bad. I'll be waiting here so\x01",
            "when you're free, come back again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "At any rate, please make it snappy.\x02",
    )

    CloseMessageWindow()
    OP_28(0x5, 0x1, 0x8000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_8C(0xD, 0, 0)
    TalkEnd(0xD)
    Jump("loc_623E")

    label("loc_623E")

    Jump("loc_60D9")

    label("loc_6241")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6661")

    label("loc_624E")

    ClearChrFlags(0xD, 0x10)

    ChrTalk(    #262
        0xFE,
        (
            "Darn bracers. How long do they\x01",
            "intend to keep me waiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "If they don't hurry and get here,\x01",
            "I'm going to miss my flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "I should have expected as much\x01",
            "from a rural backwater burg like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(400)
    TurnDirection(0xD, 0x0, 0)

    ChrTalk(    #265
        0xFE,
        "Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "Well, I'll be. That's the bracer emblem\x01",
            "if I'm not mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "I've been waiting for you to show up.\x01",
            "I have an urgent job, so do you have\x01",
            "some time to hear my request?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 0)

    label("loc_640A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6657")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Listen]\x01",            # 0
            "[Don't listen]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_6462"),
        (1, "loc_655B"),
        (SWITCH_DEFAULT, "loc_6654"),
    )


    label("loc_6462")


    ChrTalk(    #268
        0x101,
        (
            "#000FUh, sure.\x01",
            "We've got some time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #269
        0xFE,
        "Great. This really helps me out a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "All right, let me give you a rundown\x01",
            "and explain the details of the job.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6542")
    TurnDirection(0x10F, 0xD, 400)

    ChrTalk(    #271
        0x10F,
        (
            "#0142F...\x02\x03",

            "Make it quick...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6542")

    Sleep(400)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Call(0, 18)
    Jump("loc_6654")

    label("loc_655B")


    ChrTalk(    #272
        0x101,
        (
            "#505FUm, I'm sorry...\x02\x03",

            "We're still a little busy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #273
        0xFE,
        "What? Now's not a good time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "That's too bad. I'll be waiting here so\x01",
            "when you're free, come back again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "At any rate, please make it snappy.\x02",
    )

    CloseMessageWindow()
    OP_28(0x5, 0x1, 0x8000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_8C(0xD, 0, 0)
    TalkEnd(0xD)
    Jump("loc_6654")

    label("loc_6654")

    Jump("loc_640A")

    label("loc_6657")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6661")

    Jump("loc_6732")

    label("loc_6664")


    ChrTalk(    #276
        0xFE,
        (
            "Darn bracers. How long do they\x01",
            "intend to keep me waiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "If they don't hurry and get here,\x01",
            "I'm going to miss my flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "I should have expected as much\x01",
            "from a rural backwater such as\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6732")

    TalkEnd(0xD)
    Return()

    # Function_17_5060 end

    def Function_18_6736(): pass

    label("Function_18_6736")

    Fade(1000)
    EventBegin(0x0)
    SetChrPos(0x101, 38840, 0, 27320, 315)
    SetChrPos(0x102, 37840, 0, 26710, 0)
    SetChrPos(0x2, 38840, 0, 25820, 0)
    SetChrPos(0x3, 37840, 0, 25210, 0)
    OP_6D(37930, 0, 27910, 0)
    OP_6C(135000, 0)
    OP_6B(2800, 0)
    OP_6E(280, 0)
    OP_4A(0xD, 255)
    OP_8C(0xD, 180, 0)
    OP_0D()
    OP_28(0x5, 0x4, 0x4)
    OP_28(0x5, 0x4, 0x8)
    OP_28(0x5, 0x1, 0x1)

    ChrTalk(    #279
        0xFE,
        "Let me formally introduce myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "I am Orvid, representative for\x01",
            "Orvid Co., Ltd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        "#000FI'm Estelle and this is...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(    #282
        0x102,
        "#010FJoshua. It's nice to meet you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #283
        0xFE,
        (
            "Estelle and Joshua, is it?\x01",
            "The two of you are quite young\x01",
            "if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x101,
        (
            "#506FHee hee. We're actually pretty\x01",
            "new to this whole bracer thing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #285
        0xFE,
        "Greenhorns...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "...Oh well, I guess you'll\x01",
            "have to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #287
        0x101,
        "#501FPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "*cough* ...Never mind, I was just\x01",
            "talking to myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "All right, let's get down to business.\x01",
            "Please excuse my lack of decorum,\x01",
            "but I'm in a bit of a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x101,
        "#006FSure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "At the moment, I'm looking for a rare\x01",
            "mushroom called the 'Firefly Fungus'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "It is said that it only grows in soil\x01",
            "rich with septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "There are records of it being picked\x01",
            "here in Rolent, but no shops seem\x01",
            "to carry it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "However, it is of vital necessity that\x01",
            "I get my hands on one, so I put in a\x01",
            "request at the guildhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x102,
        (
            "#013FSoil rich with septium...hmm...\x01",
            "I can only think of the Malga Trail\x01",
            "as a possible location.\x02\x03",

            "#010FDo you know any other characteristics\x01",
            "of these mushrooms?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #296
        0xFE,
        (
            "It seems that it normally grows\x01",
            "in areas with patches of grass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "However, since it is buried in the dirt,\x01",
            "if you don't look closely, you won't\x01",
            "find it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #298
        0x101,
        (
            "#002FGeez, this one sounds like\x01",
            "it's going to be a pain...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #299
        0xFE,
        (
            "But, once you dig one up, you'll\x01",
            "know if it's a Firefly Fungus or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "For one thing, it glows with a\x01",
            "light green color.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x102,
        (
            "#014FSo that's why it's called a\x01",
            "'Firefly Fungus'?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #302
        0x101,
        "#000FWell, that makes sense.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #303
        0xFE,
        (
            "All right, have I explained things\x01",
            "clearly enough?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #304
        0x101,
        (
            "#006FSo basically, all we need to do is find\x01",
            "a glowing mushroom in a patch of\x01",
            "grass along the Malga Trail, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #305
        0x102,
        (
            "#010FLooks that way to me.\x02\x03",

            "Well, if they're really growing in\x01",
            "the ground, we probably won't be\x01",
            "able to find one so easily.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F7D():
        TurnDirection(0xD, 0x0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6F7D)
    Sleep(200)
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(    #306
        0xFE,
        (
            "If you run into any trouble, come\x01",
            "back and speak with me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "I ask that you find one as soon\x01",
            "as possible.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6B(3300, 0)
    OP_6E(262, 0)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    TalkEnd(0xD)
    Return()

    # Function_18_6736 end

    SaveToFile()

Try(main)
