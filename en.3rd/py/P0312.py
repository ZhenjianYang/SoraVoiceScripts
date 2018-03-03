from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P0312   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P0312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = -2980,
        TriggerZ            = 0,
        TriggerY            = 66830,
        TriggerRange        = 800,
        ActorX              = -2980,
        ActorZ              = 1000,
        ActorY              = 66830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5110,
        TriggerZ            = 0,
        TriggerY            = 65500,
        TriggerRange        = 400,
        ActorX              = -5410,
        ActorZ              = 1500,
        ActorY              = 65800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61880,
        TriggerZ            = 0,
        TriggerY            = 6590,
        TriggerRange        = 1000,
        ActorX              = 62860,
        ActorZ              = 1000,
        ActorY              = 6490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 63000,
        TriggerZ            = 0,
        TriggerY            = -42000,
        TriggerRange        = 1000,
        ActorX              = 63000,
        ActorZ              = 1000,
        ActorY              = -42000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_16A",          # 01, 1
        "Function_2_1CC",          # 02, 2
        "Function_3_300",          # 03, 3
        "Function_4_42E",          # 04, 4
        "Function_5_5B8",          # 05, 5
        "Function_6_A60",          # 06, 6
        "Function_7_AFA",          # 07, 7
        "Function_8_EC0",          # 08, 8
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_14D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_14D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_169")
    Event(0, 4)

    label("loc_169")

    Return()

    # Function_0_13A end

    def Function_1_16A(): pass

    label("Function_1_16A")

    OP_B1("P0312_2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187")
    OP_71(0x400, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()

    label("loc_187")

    OP_72(0x405, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199")
    OP_64(0x1, 0x1)

    label("loc_199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB")
    OP_6F(0x6, 0)
    Jump("loc_1B2")

    label("loc_1AB")

    OP_6F(0x6, 60)

    label("loc_1B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4")
    OP_6F(0x7, 0)
    Jump("loc_1CB")

    label("loc_1C4")

    OP_6F(0x7, 60)

    label("loc_1CB")

    Return()

    # Function_1_16A end

    def Function_2_1CC(): pass

    label("Function_2_1CC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_23A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xFC\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2692)
    Jump("loc_2A2")

    label("loc_23A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xFC\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFC\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_2A2")

    Jump("loc_2F2")

    label("loc_2A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05You found the greatest gift of all: love.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xE4, 0x0)

    label("loc_2F2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1CC end

    def Function_3_300(): pass

    label("Function_3_300")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x1E)
    OP_73(0x7)
    OP_6F(0x7, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(300)

    AnonymousTalk(    #3
        "\x07\x05Received \x07\x02300 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2693)
    Jump("loc_417")

    label("loc_36B")


    AnonymousTalk(    #4
        (
            "\x07\x05Did you know? The Trails in the Sky games now have a nifty 'Skip S-Craft'\x01",
            "feature on PC. That's not even in the original Japanese version! Isn't that\x01",
            "neato torpedo?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_417")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xE5, 0x0)
    Return()

    # Function_3_300 end

    def Function_4_42E(): pass

    label("Function_4_42E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -3030, 0, 59570, 0)
    SetChrPos(0x10F, -2610, 0, 58260, 0)
    SetChrPos(0x107, -4440, 0, 57860, 0)
    OP_6D(-2250, 0, 59900, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(45000, 0)
    OP_6E(273, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #5
        0x10F,
        "#1444FIs this some kind of factory?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        (
            "#063F#6PYep.\x02\x03",

            "It's the area where the maintenance crew\x01",
            "does all of their work. But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1065F#5P...there sure isn't anybody here right now.\x02\x03",

            "#1067FThis is bizarre... Just where did everyone go?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2614)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_42E end

    def Function_5_5B8(): pass

    label("Function_5_5B8")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, -3100, 0, 65680, 0)
    SetChrPos(0x10F, -2420, 0, 64459, 0)
    SetChrPos(0x107, -3940, 0, 64099, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_6D(-1970, 0, 66010, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(263, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #8
        0x109,
        (
            "#1079F#5POn the other side of this door is the ship's\x01",
            "engine room, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        (
            "#060FThat's right.\x02\x03",

            "The eight state-of-the-art XG-02 engines that \x01",
            "serve as its main engines are stored in here.\x02\x03",

            "#560FI'm going to go take a look at them!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetChrPos(0x109, -3700, 0, 63900, 0)
    SetChrPos(0x10F, -2650, 0, 63440, 0)
    SetChrPos(0x107, -3110, 0, 65770, 180)
    OP_6D(-1930, 0, 65600, 0)
    OP_67(0, 5570, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(263, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #10
        0x107,
        (
            "#561F#5PIt's no good... I couldn't get any of them to\x01",
            "turn on at all.\x02\x03",

            "I'm not even sure why they won't work, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        "#1067F#6PHmm... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1448F#4PWell, we already know that this place more or\x01",
            "less has its own laws.\x02\x03",

            "It wouldn't be unusual if one of those caused\x01",
            "machinery of all kinds to become nonfunctional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x107,
        (
            "#562F#5PI wish I could help you out more...\x02\x03",

            "#062FStill, I was at least able to secure a backup\x01",
            "orbal power line.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #14
        0x107,
        (
            "#560F#5PSo that computer over there should be good\x01",
            "to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1840F#6PReally? That's plenty of help, Tita.\x02\x03",

            "#1078FLet's check it out and see what it can\x01",
            "let us do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2615)
    OP_65(0x1, 0x1)
    OP_28(0x29, 0x1, 0x400)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_5_5B8 end

    def Function_6_A60(): pass

    label("Function_6_A60")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -4480, 0, 65340, 0)
    SetChrPos(0x1, -5500, 0, 65180, 0)
    SetChrPos(0x2, -4710, 0, 64260, 0)
    SetChrPos(0x3, -5830, 0, 64099, 0)
    OP_6D(-4250, 0, 66180, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_6_A60 end

    def Function_7_AFA(): pass

    label("Function_7_AFA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x0, -4480, 0, 65340, 0)
    SetChrPos(0x1, -5500, 0, 65180, 0)
    SetChrPos(0x2, -4710, 0, 64260, 0)
    SetChrPos(0x3, -5830, 0, 64099, 0)
    OP_6D(-4250, 0, 66180, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("CAPEL")
    SetMessageWindowPos(250, 78, 36, 12)

    AnonymousTalk(    #16
        (
            "\x07\x02#1SThe Orbal Calculator\x01",
            "CAPEL SYSTEM Ver.8.0\x01",
            "MODE:Security Control\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W..........#20WOK!\x01",
            "#200W　#20W\x01",
            "#1SSecurity can be disabled in event of emergency.\x01",
            "Select an area to unlock.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB4")

    Menu(
        1,
        100,
        80,
        1,
        (
            "Bridge\x01",               # 0
            "Conference Room\x01",      # 1
            "Medical Room\x01",         # 2
            "Do Nothing\x01",           # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CF0"),
        (1, "loc_D4F"),
        (2, "loc_DAE"),
        (SWITCH_DEFAULT, "loc_E96"),
    )


    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 6)), scpexpr(EXPR_END)), "loc_D30")

    AnonymousTalk(    #17
        "\x07\x02#1SThis area has already been unlocked.\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D4C")

    label("loc_D30")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_D4C")

    Jump("loc_EB1")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 7)), scpexpr(EXPR_END)), "loc_D8F")

    AnonymousTalk(    #18
        "\x07\x02#1SThis area has already been unlocked.\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DAB")

    label("loc_D8F")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/P0311   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_DAB")

    Jump("loc_EB1")

    label("loc_DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 0)), scpexpr(EXPR_END)), "loc_DEE")

    AnonymousTalk(    #19
        "\x07\x02#1SThis area has already been unlocked.\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E93")

    label("loc_DEE")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A2(0x2618)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-1630, 0, -50570, 0)
    OP_67(0, 6060, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_22(0x9C, 0x0, 0x64)
    OP_0D()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF)
    OP_73(0x3)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x1003, 0x0)
    ExitThread()
    OP_A2(0x2504)
    NewScene("ED6_DT21/P0312   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)

    label("loc_E93")

    Jump("loc_EB1")

    label("loc_E96")

    FadeToBright(300, 0)
    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EB1")

    label("loc_EB1")

    Jump("loc_C8A")

    label("loc_EB4")

    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_7_AFA end

    def Function_8_EC0(): pass

    label("Function_8_EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED1")
    Call(0, 5)
    Return()

    label("loc_ED1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #20
        (
            "\x07\x05Engine Room\x01",
            "※ Authorized personnel only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_EC0 end

    SaveToFile()

Try(main)
