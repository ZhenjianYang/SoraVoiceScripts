from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1503   ._SN',
        MapName             = 'Bose',
        Location            = 'R1503.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60022",
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
        'Royal Army Soldier',                   # 9
        'Ravennue Trail',                       # 10
        'Ravennue Trail',                       # 11
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
        Unknown_3A              = 59,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
    )

    DeclNpc(
        X                   = -112680,
        Z                   = -50,
        Y                   = 21490,
        Direction           = 180,
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
        X                   = -111060,
        Z                   = -20,
        Y                   = -19200,
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
        X                   = 1140,
        Z                   = 10,
        Y                   = -19200,
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
        X                   = -112190,
        Y                   = -1000,
        Z                   = 23280,
        Range               = -106880,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x619E,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 2000,
        TriggerZ            = 0,
        TriggerY            = 22680,
        TriggerRange        = 1700,
        ActorX              = 2100,
        ActorZ              = 1000,
        ActorY              = 23270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -114320,
        TriggerZ            = 0,
        TriggerY            = 6860,
        TriggerRange        = 1500,
        ActorX              = -114320,
        ActorZ              = 50,
        ActorY              = 6860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2180,
        TriggerZ            = 0,
        TriggerY            = 6860,
        TriggerRange        = 1500,
        ActorX              = -2180,
        ActorZ              = 50,
        ActorY              = 6860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19E",          # 00, 0
        "Function_1_1AB",          # 01, 1
        "Function_2_1F4",          # 02, 2
        "Function_3_20A",          # 03, 3
        "Function_4_272",          # 04, 4
        "Function_5_DCD",          # 05, 5
        "Function_6_F40",          # 06, 6
    )


    def Function_0_19E(): pass

    label("Function_0_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1AA")
    ClearChrFlags(0x8, 0x80)

    label("loc_1AA")

    Return()

    # Function_0_19E end

    def Function_1_1AB(): pass

    label("Function_1_1AB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1BF"),
        (101, "loc_1D9"),
        (102, "loc_1D9"),
        (SWITCH_DEFAULT, "loc_1F3"),
    )


    label("loc_1BF")

    OP_16(0x2, 0xFA0, 0xFFFE0FE8, 0xFFFE2758, 0x3006B)
    ClearChrFlags(0x9, 0x4)
    Jump("loc_1F3")

    label("loc_1D9")

    OP_16(0x2, 0xFA0, 0xFFFC5A68, 0xFFFE2758, 0x30022)
    ClearChrFlags(0xA, 0x4)
    Jump("loc_1F3")

    label("loc_1F3")

    Return()

    # Function_1_1AB end

    def Function_2_1F4(): pass

    label("Function_2_1F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_209")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1F4")

    label("loc_209")

    Return()

    # Function_2_1F4 end

    def Function_3_20A(): pass

    label("Function_3_20A")

    TalkBegin(0x8)

    ChrTalk(    #0
        0x8,
        (
            "This place is currently under\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "This area is off-limits to all\x01",
            "civilians.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_3_20A end

    def Function_4_272(): pass

    label("Function_4_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_27C")
    Jump("loc_DCC")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_END)), "loc_53D")
    EventBegin(0x0)
    OP_A2(0x31F)
    OP_28(0x36, 0x1, 0x100)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05The gate is secured with a heavy chain and padlock.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339")

    ChrTalk(    #3
        0x101,
        (
            "#000FLet's use this key we borrowed\x01",
            "from the village elder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2")

    label("loc_339")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_374")

    ChrTalk(    #4
        0x102,
        "#010FLet's use this key we borrowed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B2")

    label("loc_374")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2")

    ChrTalk(    #5
        0x103,
        "#020FAll right, let's give this key a try...\x02",
    )

    CloseMessageWindow()

    label("loc_3B2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x73, 0x0, 0x64)

    AnonymousTalk(    #6
        "\x07\x00Used \x07\x02Abandoned Mine Key\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x6E, 0x0, 0x64)
    OP_6D(-110000, 0, 21330, 0)
    SetChrPos(0x101, -110000, 0, 21330, 0)
    SetChrPos(0x102, -110700, 0, 20190, 0)
    SetChrPos(0x103, -109100, 0, 20200, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #7
        0x101,
        "#007FWhew, that was one heavy gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#012FLet's have a look inside, shall we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#022FI don't know about sky bandits, but\x01",
            "I can definitely sense monsters in\x01",
            "here.\x02\x03",

            "Everyone stay alert.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x4)
    OP_16(0x2, 0xFA0, 0xFFFC5A68, 0xFFFE2758, 0x30022)
    ClearChrFlags(0xA, 0x4)
    EventEnd(0x0)
    Jump("loc_DCC")

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_5A3")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05The gate is secured with a heavy chain and padlock.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_DCC")

    label("loc_5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_D70")
    OP_A2(0x31D)
    OP_28(0x36, 0x1, 0x20)
    OP_28(0x36, 0x1, 0x40)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(2610, 0, 22670, 0)
    SetChrPos(0x101, 2298, 0, 22143, 0)
    SetChrPos(0x102, 1217, 0, 21146, 0)
    SetChrPos(0x103, 2841, 0, 20998, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05The gate is secured with a heavy chain and padlock.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #12
        0x102,
        (
            "#010FThis looks like the entrance to\x01",
            "an abandoned mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#000FIt kind of reminds me of the\x01",
            "Malga Mine...\x02\x03",

            "Except for the fact that it's all\x01",
            "deserted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        (
            "#020FIt seems that this place was\x01",
            "abandoned quite some time ago.\x02\x03",

            "The padlock and chain are rusted.\x01",
            "It doesn't look like this gate has\x01",
            "been opened recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#013FWhich means that there's no possibility\x01",
            "that the sky bandits entered through\x01",
            "here...\x02\x03",

            "I wonder if that's why the army never\x01",
            "investigated the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#007FYou're probably not going to find\x01",
            "any clues searching around in an\x01",
            "old mine, that's for sure...\x02\x03",

            "#002F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        "#023FWhat's wrong, Estelle?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 181, 400)

    ChrTalk(    #18
        0x101,
        (
            "#002FMaybe it's just me...\x02\x03",

            "But do you feel any air flowing out\x01",
            "of here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#023FWhen you say 'out of here,' do you\x01",
            "mean the mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#002FYeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#012FLet's see...\x02",
    )

    CloseMessageWindow()

    def lambda_9A3():

        label("loc_9A3")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_9A3")

    QueueWorkItem2(0x101, 1, lambda_9A3)
    OP_8E(0x102, 0x4B0, 0x0, 0x588E, 0x7D0, 0x0)
    OP_44(0x101, 0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05Joshua wet the tip of his index finger with his tongue and held it out.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #23
        0x102,
        "#015F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #24
        0x102,
        (
            "#014FYou're right, Estelle... It's rather subtle,\x01",
            "but there is air flowing out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#501FJust like I thought, huh?\x02",
    )

    CloseMessageWindow()

    def lambda_AE4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE4)

    ChrTalk(    #26
        0x103,
        (
            "#023FSometimes your senses can be\x01",
            "surprisingly sharp, you know that?\x02\x03",

            "#021FI wonder if you get that from\x01",
            "your father.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #27
        0x101,
        (
            "#007FMy dad doesn't have anything to\x01",
            "do with it!\x02\x03",

            "#006FBut forget about that. Aren't you\x01",
            "more interested in what's inside\x01",
            "this old mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#010FThere's certainly a possibility that\x01",
            "it connects to somewhere.\x02\x03",

            "It's probably worth checking out.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #29
        0x101,
        (
            "#001FWell, in that case, let's bust\x01",
            "this lock off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        (
            "#025FHey! Don't you even think about\x01",
            "doing that!\x02\x03",

            "#020FFor now, we'd better head back to the\x01",
            "village and talk with the elder.\x02\x03",

            "He might have the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#007FHmph. You're no fun, Schera.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_DCC")

    label("loc_D70")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05The gate is secured with a heavy chain and padlock.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_DCC")

    Return()

    # Function_4_272 end

    def Function_5_DCD(): pass

    label("Function_5_DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_F3F")
    EventBegin(0x1)
    TurnDirection(0x8, 0x0, 400)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E77")

    ChrTalk(    #33
        0x8,
        (
            "How many times do you need to be\x01",
            "told that this place is off-limits?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "Do you want to get thrown in the\x01",
            "dungeon at the Haken Gate?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F12")

    label("loc_E77")

    OP_A2(0x0)

    ChrTalk(    #35
        0x8,
        (
            "Hey! This place is off-limits!\x01",
            "You're not allowed inside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "If you don't leave the premises,\x01",
            "I'll have no choice but to place\x01",
            "you under arrest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F12")


    def lambda_F18():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F18)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0x8, 255)

    label("loc_F3F")

    Return()

    # Function_5_DCD end

    def Function_6_F40(): pass

    label("Function_6_F40")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #37
        "\x07\x05Ravennue Mine\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_F40 end

    SaveToFile()

Try(main)
