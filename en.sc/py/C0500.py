from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0500   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0500.x',
        MapIndex            = 20,
        MapDefaultBGM       = "ed60031",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C0500_1 ._SN',
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
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
        'ED6_DT09/CH10110 ._CH',             # 00
        'ED6_DT09/CH10111 ._CH',             # 01
        'ED6_DT09/CH10270 ._CH',             # 02
        'ED6_DT09/CH10271 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH10110P._CP',             # 00
        'ED6_DT09/CH10111P._CP',             # 01
        'ED6_DT09/CH10270P._CP',             # 02
        'ED6_DT09/CH10271P._CP',             # 03
    )

    DeclNpc(
        X                   = -28050,
        Z                   = 1000,
        Y                   = 56920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 11000,
        Z                   = 0,
        Y                   = 0,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1000,
        Z                   = 0,
        Y                   = 14000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19000,
        Z                   = 0,
        Y                   = 29000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -28190,
        TriggerZ            = 0,
        TriggerY            = 56290,
        TriggerRange        = 1000,
        ActorX              = -28050,
        ActorZ              = 0,
        ActorY              = 56920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2210,
        TriggerZ            = 0,
        TriggerY            = 30060,
        TriggerRange        = 1000,
        ActorX              = -1530,
        ActorZ              = 0,
        ActorY              = 29870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3200,
        TriggerZ            = 0,
        TriggerY            = -17000,
        TriggerRange        = 800,
        ActorX              = 3200,
        ActorZ              = 1000,
        ActorY              = -17000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20000,
        TriggerZ            = 0,
        TriggerY            = 54040,
        TriggerRange        = 600,
        ActorX              = -20000,
        ActorZ              = 600,
        ActorY              = 54040,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15800,
        TriggerZ            = 0,
        TriggerY            = -160,
        TriggerRange        = 1000,
        ActorX              = 15800,
        ActorZ              = 1000,
        ActorY              = -160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -300,
        TriggerZ            = 0,
        TriggerY            = -10060,
        TriggerRange        = 1000,
        ActorX              = -2720,
        ActorZ              = 0,
        ActorY              = -9680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_216",          # 00, 0
        "Function_1_217",          # 01, 1
        "Function_2_2C3",          # 02, 2
        "Function_3_2D9",          # 03, 3
        "Function_4_4E0",          # 04, 4
        "Function_5_60D",          # 05, 5
        "Function_6_62F",          # 06, 6
        "Function_7_851",          # 07, 7
    )


    def Function_0_216(): pass

    label("Function_0_216")

    Return()

    # Function_0_216 end

    def Function_1_217(): pass

    label("Function_1_217")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x80)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232")
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    Jump("loc_236")

    label("loc_232")

    OP_64(0x3, 0x1)

    label("loc_236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x328, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248")
    OP_6F(0x1, 0)
    Jump("loc_24F")

    label("loc_248")

    OP_6F(0x1, 60)

    label("loc_24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x328, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261")
    OP_6F(0x2, 0)
    Jump("loc_268")

    label("loc_261")

    OP_6F(0x2, 60)

    label("loc_268")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BD")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_2BD")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_217 end

    def Function_2_2C3(): pass

    label("Function_2_2C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2C3")

    label("loc_2D8")

    Return()

    # Function_2_2C3 end

    def Function_3_2D9(): pass

    label("Function_3_2D9")

    OP_EA(0x2, 0x9, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x328, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_474")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x328, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_330():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_330)

    def lambda_34B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_34B)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x2E, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_39E"),
        (2, "loc_3B0"),
        (1, "loc_3C0"),
        (SWITCH_DEFAULT, "loc_3C3"),
    )


    label("loc_39E")

    OP_A2(0x1941)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_3C3")

    label("loc_3B0")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_3C0")

    OP_B4(0x0)
    Return()

    label("loc_3C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x284, 1)"), scpexpr(EXPR_END)), "loc_40F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found \x1F\x84\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1940)
    Jump("loc_471")

    label("loc_40F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "Found \x1F\x84\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x84\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_471")

    Jump("loc_4D2")

    label("loc_474")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "\x07\x05I hate to tell you this, but you've already cleaned\x01",
            "this one out.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4D2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2D9 end

    def Function_4_4E0(): pass

    label("Function_4_4E0")

    OP_EA(0x2, 0x13, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x328, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_551")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1942)
    Jump("loc_5B5")

    label("loc_551")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_5B5")

    Jump("loc_5FF")

    label("loc_5B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05<YOU HAVE ACTIVATED THE STARING CONTEST>\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5FF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4E0 end

    def Function_5_60D(): pass

    label("Function_5_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_625")
    NewScene("ED6_DT21/T0101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_62E")

    label("loc_625")

    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_62E")

    Return()

    # Function_5_60D end

    def Function_6_62F(): pass

    label("Function_6_62F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_695")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_850")

    label("loc_695")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_835")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 15800, 1000, -160, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x32)
    OP_73(0x3)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 15800, 1000, -160, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_835")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_84F")

    Return()

    label("loc_850")

    Return()

    # Function_6_62F end

    def Function_7_851(): pass

    label("Function_7_851")

    EventBegin(0x1)

    ChrTalk(    #9
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_87D():
        OP_6D(-1040, 0, -9430, 700)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_87D)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #10
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x4, 0x1FE, 0x0, 0xFFFFD922, 0x10E, 0xFFFFF560, 0xFFFFFC18, 0xFFFFDA30)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_9CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x80)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C6")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x80)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Recorded Rolent Sewers fishing spot in Bracer Notebook.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_9C6")

    Jump("loc_9CF")

    label("loc_9C9")

    OP_28(0x73, 0x1, 0x200)

    label("loc_9CF")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_9E4")

    label("loc_9D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E4")
    EventEnd(0x1)

    label("loc_9E4")

    Return()

    # Function_7_851 end

    SaveToFile()

Try(main)
