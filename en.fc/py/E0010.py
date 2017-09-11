from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0010   ._SN',
        MapName             = 'event',
        Location            = 'E0010.x',
        MapIndex            = 49,
        MapDefaultBGM       = "ed60030",
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
        Unknown_3A              = 49,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = 58996,
        TriggerZ            = -448,
        TriggerY            = 48932,
        TriggerRange        = 1700,
        ActorX              = 58920,
        ActorZ              = -200,
        ActorY              = 49040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59075,
        TriggerZ            = -2000,
        TriggerY            = 54692,
        TriggerRange        = 1700,
        ActorX              = 59075,
        ActorZ              = -1600,
        ActorY              = 54692,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25983,
        TriggerZ            = 200,
        TriggerY            = -8664,
        TriggerRange        = 1700,
        ActorX              = 25510,
        ActorZ              = 1200,
        ActorY              = -8070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 84719,
        TriggerZ            = 0,
        TriggerY            = 44588,
        TriggerRange        = 1700,
        ActorX              = 84719,
        ActorZ              = 2000,
        ActorY              = 44588,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 89364,
        TriggerZ            = -1000,
        TriggerY            = 53636,
        TriggerRange        = 1700,
        ActorX              = 89364,
        ActorZ              = -600,
        ActorY              = 53636,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33110,
        TriggerZ            = 0,
        TriggerY            = 5650,
        TriggerRange        = 1700,
        ActorX              = 33110,
        ActorZ              = 1500,
        ActorY              = 5650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_182",          # 00, 0
        "Function_1_1BC",          # 01, 1
        "Function_2_1E1",          # 02, 2
        "Function_3_3A2",          # 03, 3
        "Function_4_4D6",          # 04, 4
        "Function_5_5BD",          # 05, 5
        "Function_6_6F6",          # 06, 6
        "Function_7_7F5",          # 07, 7
        "Function_8_8F7",          # 08, 8
    )


    def Function_0_182(): pass

    label("Function_0_182")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_19A"),
        (109, "loc_1A9"),
        (115, "loc_1AF"),
        (105, "loc_1B5"),
        (SWITCH_DEFAULT, "loc_1BB"),
    )


    label("loc_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6")
    Event(0, 2)

    label("loc_1A6")

    Jump("loc_1BB")

    label("loc_1A9")

    OP_A2(0x323)
    Jump("loc_1BB")

    label("loc_1AF")

    OP_A2(0x324)
    Jump("loc_1BB")

    label("loc_1B5")

    OP_A2(0x325)
    Jump("loc_1BB")

    label("loc_1BB")

    Return()

    # Function_0_182 end

    def Function_1_1BC(): pass

    label("Function_1_1BC")

    OP_72(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_END)), "loc_1E0")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)

    label("loc_1E0")

    Return()

    # Function_1_1BC end

    def Function_2_1E1(): pass

    label("Function_2_1E1")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(30980, 0, -4620, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 27350, 0, 5680, 103)
    SetChrPos(0x102, 26450, 0, 5010, 114)
    SetChrPos(0x103, 27280, 0, 4760, 101)

    def lambda_25E():
        OP_6C(65000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25E)
    OP_6D(29950, 0, 4840, 4000)

    ChrTalk(    #0
        0x101,
        (
            "#505FWow...it's pretty bare in here.\x02\x03",

            "There's not a piece of cargo left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#013FEvidently, the sky bandits managed\x01",
            "to make off with it all.\x02\x03",

            "At least, judging by the looks\x01",
            "of things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x103,
        (
            "#022FAt any rate, we should do a\x01",
            "thorough investigation of the\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38B():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38B)
    OP_69(0x0, 0x5DC)
    OP_A2(0x321)
    EventEnd(0x0)
    Return()

    # Function_2_1E1 end

    def Function_3_3A2(): pass

    label("Function_3_3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464")
    EventBegin(0x0)
    OP_6D(58996, -448, 48932, 1000)

    ChrTalk(    #3
        0x101,
        (
            "#501FIt looks like this is the captain's\x01",
            "seat.\x02\x03",

            "#007FIf these were any other circumstances,\x01",
            "I would love to sit here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        "#018FDon't even think about it.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_4D2")

    label("loc_464")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05It doesn't look like anyone's been\x01",
            "in this chair for quite some time.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_4D2")

    OP_A2(0x0)
    Return()

    # Function_3_3A2 end

    def Function_4_4D6(): pass

    label("Function_4_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_560")
    EventBegin(0x0)
    OP_6D(59075, -2000, 54692, 1000)

    ChrTalk(    #6
        0x101,
        (
            "#505FHere's the steering wheel used\x01",
            "to pilot the ship.\x02\x03",

            "I wonder where the pilot could\x01",
            "have gone...?\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_5B9")

    label("loc_560")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05There's a steering wheel to control\x01",
            "the rudders.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_5B9")

    OP_A2(0x1)
    Return()

    # Function_4_4D6 end

    def Function_5_5BD(): pass

    label("Function_5_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66D")
    EventBegin(0x0)
    OP_6D(25983, 200, -8664, 1000)

    ChrTalk(    #8
        0x101,
        "#004FI wonder what this is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#022FIt's the orbal engine control\x01",
            "panel.\x02\x03",

            "It looks like the flow of orbal\x01",
            "energy has completely stopped.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_6F2")

    label("loc_66D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05There's an orbal engine control\x01",
            "panel.\x02\x03",

            "The orbal energy appears to have\x01",
            "completely stopped.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_6F2")

    OP_A2(0x2)
    Return()

    # Function_5_5BD end

    def Function_6_6F6(): pass

    label("Function_6_6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AE")
    EventBegin(0x0)
    OP_6D(33110, 0, 5650, 1000)

    ChrTalk(    #11
        0x101,
        "#004FHere's a lift car.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#012FIt looks like the same type as\x01",
            "those at the landing port.\x02\x03",

            "The sky bandits probably used\x01",
            "this to move the cargo.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_7F1")

    label("loc_7AE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05There is a cargo lift car.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_7F1")

    OP_A2(0x5)
    Return()

    # Function_6_6F6 end

    def Function_7_7F5(): pass

    label("Function_7_7F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AD")
    EventBegin(0x0)
    OP_6D(84719, 1000, 44588, 1000)

    ChrTalk(    #14
        0x101,
        (
            "#505FThis poor potted plant doesn't\x01",
            "look like it's gonna make it...\x01",
            "Bunch'a plant murderers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#012FIt probably hasn't been watered\x01",
            "for days.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_8F3")

    label("loc_8AD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05The plant is slightly wilted.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_8F3")

    OP_A2(0x3)
    Return()

    # Function_7_7F5 end

    def Function_8_8F7(): pass

    label("Function_8_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96A")
    EventBegin(0x0)
    OP_6D(89364, -600, 53636, 1000)

    ChrTalk(    #17
        0x101,
        (
            "#003FIt's bright in here... There's a lot\x01",
            "of light shining into this place...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_9B4")

    label("loc_96A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Light is shining in from outside.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_9B4")

    OP_A2(0x4)
    Return()

    # Function_8_8F7 end

    SaveToFile()

Try(main)
