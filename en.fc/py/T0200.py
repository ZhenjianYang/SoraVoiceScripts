from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0200   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0200.x',
        MapIndex            = 12,
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
        'Josette',                              # 9
        'Downtown Rolent',                      # 10
    )

    DeclEntryPoint(
        Unknown_00              = -6100,
        Unknown_04              = 0,
        Unknown_08              = 50,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
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
        Unknown_3A              = 12,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = -6100,
        Unknown_04              = 0,
        Unknown_08              = 50,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
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
        Unknown_3A              = 12,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02330 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02330P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -20690,
        Z                   = 0,
        Y                   = -180,
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
        TriggerX            = 13870,
        TriggerZ            = 3700,
        TriggerY            = -4460,
        TriggerRange        = 500,
        ActorX              = 13870,
        ActorZ              = 4200,
        ActorY              = -4460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8189,
        TriggerZ            = 450,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 8189,
        ActorZ              = 1450,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_17E",          # 00, 0
        "Function_1_1B5",          # 01, 1
        "Function_2_216",          # 02, 2
        "Function_3_379",          # 03, 3
        "Function_4_98B",          # 04, 4
    )


    def Function_0_17E(): pass

    label("Function_0_17E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_191")
    OP_64(0x0, 0x1)
    Jump("loc_191")

    label("loc_191")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1A1"),
        (103, "loc_1A8"),
        (SWITCH_DEFAULT, "loc_1B4"),
    )


    label("loc_1A1")

    Event(0, 3)
    Jump("loc_1B4")

    label("loc_1A8")

    OP_6C(225000, 0)
    Jump("loc_1B4")

    label("loc_1B4")

    Return()

    # Function_0_17E end

    def Function_1_1B5(): pass

    label("Function_1_1B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CD")
    OP_B1("t0200_y")
    Jump("loc_1D6")

    label("loc_1CD")

    OP_B1("t0200_n")

    label("loc_1D6")

    OP_16(0x2, 0xFA0, 0xFFFE36F8, 0xFFFE0C00, 0x30002)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FC")
    OP_72(0x0, 0x10)
    Jump("loc_200")

    label("loc_1FC")

    OP_64(0x1, 0x1)

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_215")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_215")

    Return()

    # Function_1_1B5 end

    def Function_2_216(): pass

    label("Function_2_216")

    EventBegin(0x0)
    OP_6D(13870, 3700, -4460, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA")

    ChrTalk(    #0
        0x101,
        (
            "#004FLook, there are some marks\x01",
            "on this railing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#012FYou're right. And they're fresh,\x01",
            "too.\x02\x03",

            "#012FIt looks like something metal\x01",
            "dug into the wood.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x260)
    OP_28(0x1A, 0x1, 0x80)
    Jump("loc_376")

    label("loc_2DA")


    ChrTalk(    #2
        0x101,
        (
            "#002FHmmm...\x01",
            "Something metal and strong enough\x01",
            "to leave marks, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#012FThis seems like something worth jotting\x01",
            "down in our Bracer Notebooks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376")

    EventEnd(0x1)
    Return()

    # Function_2_216 end

    def Function_3_379(): pass

    label("Function_3_379")

    EventBegin(0x0)
    OP_A2(0x24F)
    OP_28(0x3, 0x4, 0x10)
    OP_28(0x3, 0x1, 0x200)
    OP_28(0x3, 0x1, 0x400)
    OP_28(0x4, 0x4, 0x40)
    OP_28(0x6, 0x4, 0x40)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    OP_6D(2040, 0, 650, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 1770, 0, 690, 270)
    SetChrPos(0x102, 1640, 0, -790, 270)
    SetChrPos(0x8, -450, 0, -60, 90)
    OP_6D(750, 0, -40, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #4
        0x101,
        (
            "#000FSo you're heading home tomorrow\x01",
            "on the airliner, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#217FYes, that's right.\x01",
            "School's about to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#010F#4PI see. So you used your school\x01",
            "vacation time to come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#007FThat's too bad. We could\x01",
            "have made great friends.\x02\x03",

            "#000FI hope we can meet again\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#217FThere's nothing I would\x01",
            "like more.\x02\x03",

            "#218FPlease have a wonderful day,\x01",
            "Estelle, Joshua.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_8E(0x8, 0xFFFFDC4C, 0x0, 0x118, 0xBB8, 0x0)

    ChrTalk(    #9
        0x101,
        (
            "#001FWhat a nice girl.\x02\x03",

            "#001FFor looking like someone from\x01",
            "a rich family she wasn't snooty\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        "#013F#4PYeah...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #11
        0x101,
        (
            "#004FJoshua?\x02\x03",

            "#006F...Oh?\x01",
            "Could I be correct in assuming that...\x02\x03",

            "#006F...she's your type?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#014F#4PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #13
        0x102,
        "#012F#4PWh-What are you talking about?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#006FYou're blushing!\x02\x03",

            "#001FI'm really surprised!\x02\x03",

            "#001FI had no idea that you were\x01",
            "into the rich girl type.\x02\x03",

            "#001FWe'll have to get some pick-up\x01",
            "lines ready for the next time\x01",
            "you meet.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x102,
        (
            "#018F#4PQuit getting all excited\x01",
            "about nothing.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #16
        0x102,
        (
            "#013F#4PEspecially when you have no\x01",
            "idea what others are thinking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#015F#4PJust never mind...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #19
        0x102,
        (
            "#010F#4PAnyway, let's report to the guild.\x02\x03",

            "The next job we're doing for\x01",
            "Dad will be the last one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#004FOh, right...\x02\x03",

            "#001FAll right, let's get pumped and\x01",
            "knock this last one out!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_3_379 end

    def Function_4_98B(): pass

    label("Function_4_98B")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05The front door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_98B end

    SaveToFile()

Try(main)
