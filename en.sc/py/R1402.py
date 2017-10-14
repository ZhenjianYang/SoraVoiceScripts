from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1402   ._SN',
        MapName             = 'Bose',
        Location            = 'R1402.x',
        MapIndex            = 58,
        MapDefaultBGM       = "ed60029",
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
        'New Ansel Path',                       # 9
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


    DeclNpc(
        X                   = 1070,
        Z                   = -600,
        Y                   = -32720,
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
        X                   = -3000,
        Y                   = -2000,
        Z                   = -22500,
        Range               = 5000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFFADF8,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -16000,
        Y                   = -3500,
        Z                   = 5000,
        Range               = 29380,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x251C,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -2200,
        Y                   = 3000,
        Z                   = 19000,
        Range               = 4200,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x4E20,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )


    DeclActor(
        TriggerX            = -13360,
        TriggerZ            = 40,
        TriggerY            = -930,
        TriggerRange        = 1000,
        ActorX              = -14080,
        ActorZ              = 40,
        ActorY              = -960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26480,
        TriggerZ            = -20,
        TriggerY            = 8820,
        TriggerRange        = 1000,
        ActorX              = 27130,
        ActorZ              = -20,
        ActorY              = 8920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14820,
        TriggerZ            = 40,
        TriggerY            = -10480,
        TriggerRange        = 1000,
        ActorX              = 14240,
        ActorZ              = 40,
        ActorY              = -10750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_196",          # 00, 0
        "Function_1_295",          # 01, 1
        "Function_2_380",          # 02, 2
        "Function_3_381",          # 03, 3
        "Function_4_4A0",          # 04, 4
        "Function_5_5F1",          # 05, 5
        "Function_6_88F",          # 06, 6
        "Function_7_963",          # 07, 7
        "Function_8_CD3",          # 08, 8
        "Function_9_D59",          # 09, 9
        "Function_10_DE8",         # 0A, 10
        "Function_11_EC6",         # 0B, 11
        "Function_12_F4B",         # 0C, 12
        "Function_13_FD0",         # 0D, 13
        "Function_14_1055",        # 0E, 14
        "Function_15_10DA",        # 0F, 15
        "Function_16_1266",        # 10, 16
        "Function_17_12C7",        # 11, 17
        "Function_18_1328",        # 12, 18
        "Function_19_1389",        # 13, 19
    )


    def Function_0_196(): pass

    label("Function_0_196")

    OP_A3(0x1BA0)
    OP_A3(0x1BA1)
    OP_A3(0x1BA2)
    OP_A3(0x1BA3)
    OP_A3(0x1BA4)
    OP_A3(0x1BA5)
    OP_A3(0x1BA6)
    OP_A3(0x1BA7)
    OP_A3(0x1BA8)
    OP_A3(0x1BA9)
    OP_A3(0x1BAA)
    OP_A3(0x1BAB)
    OP_A3(0x1BAC)
    OP_A3(0x1FDE)
    OP_A3(0x1FDF)
    OP_A3(0x1FE0)
    OP_A3(0x1FE1)
    OP_A3(0x1FE2)
    OP_A3(0x1FE3)
    OP_A3(0x1FE4)
    OP_A3(0x1FE5)
    OP_A3(0x1FE6)
    OP_A3(0x1FE7)
    OP_A3(0x1FE8)
    OP_A3(0x1FE9)
    OP_A3(0x1FEA)
    OP_A3(0x1FEB)
    OP_A3(0x1FEC)
    OP_A3(0x1FED)
    OP_A3(0x1FEE)
    OP_A3(0x1FEF)
    OP_A3(0x1FF0)
    OP_A3(0x1FF1)
    OP_A3(0x1FF2)
    OP_A3(0x1FF3)
    OP_A3(0x1FF4)
    OP_A3(0x1FF5)
    OP_A3(0x1FF6)
    OP_A3(0x1FF7)
    OP_A3(0x1FF8)
    OP_A3(0x1FF9)
    OP_A3(0x1FFA)
    OP_A3(0x1FFB)
    OP_A3(0x1FFC)
    OP_A3(0x1FFD)
    OP_A3(0x1FFE)
    OP_A3(0x1FFF)
    OP_A3(0x1E80)
    OP_A3(0x1E81)
    OP_A3(0x1E82)
    OP_A3(0x1E83)
    OP_A3(0x1E84)
    OP_A3(0x1E85)
    OP_A3(0x1E86)
    OP_A3(0x1E87)
    OP_A3(0x1E88)
    OP_A3(0x1E89)
    OP_A3(0x1E8A)
    OP_A3(0x1E8B)
    OP_A3(0x1E8C)
    OP_A3(0x1E8D)
    OP_A3(0x1E8E)
    OP_A3(0x1E8F)
    OP_A3(0x1E90)
    OP_A3(0x1E91)
    OP_A3(0x1E92)
    OP_A3(0x1E93)
    OP_A3(0x1E94)
    OP_A3(0x1E95)
    OP_A3(0x1E96)
    OP_A3(0x1E97)
    OP_A3(0x1E98)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_284")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 5)
    Jump("loc_294")

    label("loc_284")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    Event(0, 15)

    label("loc_294")

    Return()

    # Function_0_196 end

    def Function_1_295(): pass

    label("Function_1_295")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x23001E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x369, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B9")
    OP_6F(0x1, 0)
    Jump("loc_2C0")

    label("loc_2B9")

    OP_6F(0x1, 60)

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x369, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2")
    OP_6F(0x2, 0)
    Jump("loc_2D9")

    label("loc_2D2")

    OP_6F(0x2, 60)

    label("loc_2D9")

    OP_64(0x0, 0x1)
    OP_71(0x0, 0x0)
    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_301")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_301")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_310")
    Jump("loc_360")

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_360")
    LoadEffect(0x0, "map\\\\mp086_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 1000, 6000, 19900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_360")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_379")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_37F")

    label("loc_379")

    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)

    label("loc_37F")

    Return()

    # Function_1_295 end

    def Function_2_380(): pass

    label("Function_2_380")

    Return()

    # Function_2_380 end

    def Function_3_381(): pass

    label("Function_3_381")

    OP_EA(0x2, 0xD6, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x369, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_459")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_3F2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B48)
    Jump("loc_456")

    label("loc_3F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_456")

    Jump("loc_492")

    label("loc_459")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Wow! Look at all this air!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_492")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_381 end

    def Function_4_4A0(): pass

    label("Function_4_4A0")

    OP_EA(0x2, 0xD7, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x369, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_578")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_511")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B49)
    Jump("loc_575")

    label("loc_511")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_575")

    Jump("loc_5E3")

    label("loc_578")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05You took a gamble on something being in this\x01",
            "chest, and I'm afraid you lost.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4A0 end

    def Function_5_5F1(): pass

    label("Function_5_5F1")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_608")
    Call(0, 8)
    Call(0, 9)

    label("loc_608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FD")
    OP_6D(1390, 400, 7280, 0)
    OP_67(0, 15420, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(45000, 0)
    OP_6E(330, 0)
    StopSound(0x8CA0, 0x30D40, 0x0)
    SetChrPos(0x101, 2390, -280, -23110, 0)
    SetChrPos(0x102, 1220, -490, -23160, 0)
    SetChrPos(0xF8, 2400, -310, -24380, 0)
    SetChrPos(0xF9, 1020, -490, -24400, 0)

    def lambda_6A4():
        OP_6D(950, -20, -15430, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A4)
    OP_C8(0x200, 0x46, "C_PLAC21._CH", 0x0, 0x3E8)
    OP_DE("Amberl Tower")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    def lambda_6EE():
        OP_8E(0xFE, 0x726, 0xA, 0xFFFFBFB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6EE)

    def lambda_709():
        OP_8E(0xFE, 0x1F4, 0xFFFFFFEC, 0xFFFFBEE2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_709)

    def lambda_724():
        OP_8E(0xFE, 0x7BC, 0x28, 0xFFFFBA82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_724)

    def lambda_73F():
        OP_8E(0xFE, 0x1C2, 0xA, 0xFFFFB956, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_73F)
    WaitChrThread(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(0x8CA0, 0x186A0, 0x0)
    OP_6D(1350, -40, -18500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    SetChrPos(0x0, 1350, -40, -20010, 0)
    SetChrPos(0x1, 1350, -40, -20010, 0)
    SetChrPos(0x2, 1350, -40, -20010, 0)
    SetChrPos(0x3, 1350, -40, -20010, 0)
    OP_A2(0x1E1F)
    Jump("loc_87E")

    label("loc_7FD")

    OP_6D(1350, -40, -18500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1350, -40, -20010, 0)
    SetChrPos(0x1, 1350, -40, -20010, 0)
    SetChrPos(0x2, 1350, -40, -20010, 0)
    SetChrPos(0x3, 1350, -40, -20010, 0)

    label("loc_87E")

    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_5_5F1 end

    def Function_6_88F(): pass

    label("Function_6_88F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A1")
    Return()

    label("loc_8A1")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Return to the Arseille?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Return]\x01",            # 0
            "[Don't Return]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_942")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_962")

    label("loc_942")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_962")

    Return()

    # Function_6_88F end

    def Function_7_963(): pass

    label("Function_7_963")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_973")
    Return()

    label("loc_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 0)), scpexpr(EXPR_END)), "loc_97B")
    Return()

    label("loc_97B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A0")
    Call(0, 8)
    Call(0, 9)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_9A0")

    Fade(1000)
    OP_6D(1350, 2800, 13070, 0)
    OP_67(0, 2270, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(9000, 0)
    OP_6E(463, 0)
    SetChrPos(0x101, 1750, 400, 7850, 0)
    SetChrPos(0x102, 240, 400, 7460, 0)
    SetChrPos(0xF8, 2000, 50, 6000, 0)
    SetChrPos(0xF9, 590, 10, 6000, 0)
    OP_0D()

    ChrTalk(    #7
        0x101,
        (
            "#1015F#2PThe last tower, finally...\x02\x03",

            "#1007FYou think they might be nice twice\x01",
            "in a row and give us a straight\x01",
            "path so we don't get lost?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1035F#5PIt won't be so nice if they use powerful\x01",
            "guardians instead of sharp turns.\x02\x03",

            "#1042FIt will be dark soon. We should\x01",
            "hurry as quickly as we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1003F#2PYeah, we've got to stop Renne.\x02\x03",

            "#1002FEveryone...come on! Let's do this!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC6")

    ChrTalk(    #10
        0x107,
        "#062FYeah!\x02",
    )

    CloseMessageWindow()

    label("loc_BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE5")

    ChrTalk(    #11
        0x105,
        "#042FLet's!\x02",
    )

    CloseMessageWindow()

    label("loc_BE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C04")

    ChrTalk(    #12
        0x103,
        "#022FC'mon!\x02",
    )

    CloseMessageWindow()

    label("loc_C04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2F")

    ChrTalk(    #13
        0x109,
        "#1063FRight behind you!\x02",
    )

    CloseMessageWindow()

    label("loc_C2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4E")

    ChrTalk(    #14
        0x106,
        "#057FRight!\x02",
    )

    CloseMessageWindow()

    label("loc_C4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6D")

    ChrTalk(    #15
        0x108,
        "#072FRight!\x02",
    )

    CloseMessageWindow()

    label("loc_C6D")


    def lambda_C73():
        OP_69(0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_C73)

    def lambda_C81():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C81)

    def lambda_C99():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_C99)

    def lambda_CA9():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_CA9)

    def lambda_CB9():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_CB9)
    OP_A2(0x1E20)
    WaitChrThread(0x0, 0x0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_7_963 end

    def Function_8_CD3(): pass

    label("Function_8_CD3")

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
        (0, "loc_D4C"),
        (1, "loc_D52"),
        (SWITCH_DEFAULT, "loc_D58"),
    )


    label("loc_D4C")

    OP_A2(0x1200)
    Jump("loc_D58")

    label("loc_D52")

    OP_A2(0x1201)
    Jump("loc_D58")

    label("loc_D58")

    Return()

    # Function_8_CD3 end

    def Function_9_D59(): pass

    label("Function_9_D59")

    FadeToDark(0, 0, -1)
    OP_6D(-31870, 10, -30550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_9_D59 end

    def Function_10_DE8(): pass

    label("Function_10_DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC5")
    EventBegin(0x0)
    Fade(500)
    OP_6D(610, 4000, 21090, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x101, 500, 4000, 18000, 0)
    SetChrPos(0x102, 1500, 4000, 18000, 0)
    SetChrPos(0xF8, 500, 4000, 17000, 0)
    SetChrPos(0xF9, 1500, 4000, 17000, 0)
    OP_43(0x101, 0x0, 0x0, 0xB)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0xD)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0xE)
    WaitChrThread(0xF9, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/C1700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_EC5")

    Return()

    # Function_10_DE8 end

    def Function_11_EC6(): pass

    label("Function_11_EC6")

    OP_91(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_F0B():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F0B)

    def lambda_F25():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F25)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_11_EC6 end

    def Function_12_F4B(): pass

    label("Function_12_F4B")

    OP_91(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_F90():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F90)

    def lambda_FAA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FAA)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_12_F4B end

    def Function_13_FD0(): pass

    label("Function_13_FD0")

    OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1015():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1015)

    def lambda_102F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_102F)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_13_FD0 end

    def Function_14_1055(): pass

    label("Function_14_1055")

    OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_109A():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_109A)

    def lambda_10B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10B4)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_14_1055 end

    def Function_15_10DA(): pass

    label("Function_15_10DA")

    EventBegin(0x0)
    OP_6D(610, 4000, 21090, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x101, 1500, 4400, 20500, 180)
    SetChrPos(0x102, 500, 4400, 20500, 180)
    SetChrPos(0xF8, 1500, 4400, 20500, 180)
    SetChrPos(0xF9, 500, 4400, 20500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0x10)
    Sleep(800)
    OP_43(0x102, 0x0, 0x0, 0x11)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x12)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x13)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(1110, 4000, 17770, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1110, 4000, 17770, 180)
    SetChrPos(0x1, 1110, 4000, 17770, 180)
    SetChrPos(0x2, 1110, 4000, 17770, 180)
    SetChrPos(0x3, 1110, 4000, 17770, 180)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_10DA end

    def Function_16_1266(): pass

    label("Function_16_1266")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1271():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1271)

    def lambda_128B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_128B)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_12AC():
        OP_8F(0xFE, 0x5DC, 0xE10, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12AC)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_16_1266 end

    def Function_17_12C7(): pass

    label("Function_17_12C7")

    OP_22(0x99, 0x0, 0x64)

    def lambda_12D2():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12D2)

    def lambda_12EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12EC)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_130D():
        OP_8F(0xFE, 0x1F4, 0xE10, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_130D)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_17_12C7 end

    def Function_18_1328(): pass

    label("Function_18_1328")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1333():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1333)

    def lambda_134D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_134D)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_136E():
        OP_8F(0xFE, 0x5DC, 0xE10, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_136E)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_18_1328 end

    def Function_19_1389(): pass

    label("Function_19_1389")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1394():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1394)

    def lambda_13AE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13AE)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_13CF():
        OP_8F(0xFE, 0x1F4, 0xE10, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13CF)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_19_1389 end

    SaveToFile()

Try(main)
