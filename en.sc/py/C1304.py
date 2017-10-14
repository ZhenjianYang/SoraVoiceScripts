from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1304   ._SN',
        MapName             = 'Bose',
        Location            = 'C1304.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60089",
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
        'Dorothy',                              # 9
        'Major Vander',                         # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Food',                                 # 16
        'Food',                                 # 17
        'Gas Bomb',                             # 18
        'Gas Bomb Target',                      # 19
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
        'ED6_DT07/CH02073 ._CH',             # 00
        'ED6_DT27/CH03573 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
        'ED6_DT06/CH20020 ._CH',             # 04
        'ED6_DT07/CH00324 ._CH',             # 05
        'ED6_DT06/CH20043 ._CH',             # 06
        'ED6_DT27/CH03015 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02073P._CP',             # 00
        'ED6_DT27/CH03573P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
        'ED6_DT06/CH20020P._CP',             # 04
        'ED6_DT07/CH00324P._CP',             # 05
        'ED6_DT06/CH20043P._CP',             # 06
        'ED6_DT27/CH03015P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 524292,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524292,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1310724,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1310724,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -56680,
        TriggerZ            = 0,
        TriggerY            = -43550,
        TriggerRange        = 1000,
        ActorX              = -57380,
        ActorZ              = 0,
        ActorY              = -43550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -52110,
        TriggerZ            = 0,
        TriggerY            = -41540,
        TriggerRange        = 1000,
        ActorX              = -52130,
        ActorZ              = 0,
        ActorY              = -40880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_2C3",          # 01, 1
        "Function_2_37D",          # 02, 2
        "Function_3_4D9",          # 03, 3
        "Function_4_630",          # 04, 4
        "Function_5_742",          # 05, 5
        "Function_6_B69",          # 06, 6
        "Function_7_B87",          # 07, 7
        "Function_8_BCF",          # 08, 8
        "Function_9_C1E",          # 09, 9
        "Function_10_C6D",         # 0A, 10
        "Function_11_CBC",         # 0B, 11
        "Function_12_D38",         # 0C, 12
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2A3")
    OP_A3(0x10F0)
    Event(0, 12)
    Jump("loc_2C2")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_2B4")
    OP_A3(0x10F1)
    Event(0, 4)
    Jump("loc_2C2")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_2C2")
    OP_A3(0x10F2)
    Event(0, 5)

    label("loc_2C2")

    Return()

    # Function_0_292 end

    def Function_1_2C3(): pass

    label("Function_1_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x321, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D5")
    OP_6F(0x3, 0)
    Jump("loc_2DC")

    label("loc_2D5")

    OP_6F(0x3, 60)

    label("loc_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x321, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE")
    OP_6F(0x4, 0)
    Jump("loc_2F5")

    label("loc_2EE")

    OP_6F(0x4, 60)

    label("loc_2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 2)), scpexpr(EXPR_END)), "loc_37C")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    SetChrPos(0xB, -52060, 0, -95510, 135)
    SetChrPos(0xC, -49600, 0, -95370, 180)
    SetChrPos(0xD, -50540, 0, -96510, 0)
    SetChrPos(0xE, -50810, 0, -94450, 90)
    SetChrChipByIndex(0xB, 6)
    SetChrChipByIndex(0xC, 6)
    SetChrChipByIndex(0xD, 6)
    SetChrChipByIndex(0xE, 6)

    label("loc_37C")

    Return()

    # Function_1_2C3 end

    def Function_2_37D(): pass

    label("Function_2_37D")

    OP_EA(0x2, 0x48, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x321, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_455")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x135, 1)"), scpexpr(EXPR_END)), "loc_3EE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x35\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x190A)
    Jump("loc_452")

    label("loc_3EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x35\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x35\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_452")

    Jump("loc_4CB")

    label("loc_455")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You got away with running your hands down\x01",
            "this random chest once. Don't push your luck.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4CB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_37D end

    def Function_3_4D9(): pass

    label("Function_3_4D9")

    OP_EA(0x2, 0x49, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x321, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_54A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x190B)
    Jump("loc_5AE")

    label("loc_54A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_5AE")

    Jump("loc_622")

    label("loc_5B1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Inside the chest is emptiness. That's all there\x01",
            "ever is. Eternal and interminable.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_622")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4D9 end

    def Function_4_630(): pass

    label("Function_4_630")

    EventBegin(0x0)
    OP_6D(-50630, 0, -95070, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0xB, -52060, 0, -95510, 90)
    SetChrPos(0xC, -49600, 0, -95370, 270)
    SetChrPos(0xD, -50540, 0, -96510, 0)
    SetChrPos(0xE, -50810, 0, -94450, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0xB,
        "#6PRight. Almost time for a guard change.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        "Time to make my way over there.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1306   ._SN", 137, 0, 0)
    IdleLoop()
    Return()

    # Function_4_630 end

    def Function_5_742(): pass

    label("Function_5_742")

    EventBegin(0x0)
    OP_6D(-50630, 0, -95070, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0xB, -52060, 0, -95510, 90)
    SetChrPos(0xC, -49600, 0, -95370, 270)
    SetChrPos(0xD, -50540, 0, -96510, 0)
    SetChrPos(0xE, -50810, 0, -94450, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    LoadEffect(0x0, "map\\\\mp004_00.eff")
    SetChrPos(0x11, -51470, 0, -100000, 0)
    SetChrPos(0x12, -50830, 0, -95400, 0)
    PlayEffect(0x0, 0xFF, 0x11, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #8 op#A
        0xE,
        "#3AHmm?\x02",
    )

    Sleep(300)

    ChrTalk(    #9 op#A
        0xC,
        "#5AWhat the--?!\x02",
    )

    Sleep(200)
    OP_22(0x7F, 0x0, 0x64)
    Sleep(300)
    OP_56(0x0)
    Sleep(300)
    OP_43(0xB, 0x1, 0x0, 0xB)
    Sleep(100)

    ChrTalk(    #10 op#A
        0xE,
        "#1P#6AAgh!\x02",
    )

    Sleep(600)

    ChrTalk(    #11 op#A
        0xB,
        "#12AWh... Whaaat...?\x02",
    )

    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(1000)
    OP_56(0x0)
    Sleep(500)

    ChrTalk(    #12
        0xC,
        "Can't...stay awake...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 135, 400)
    Sleep(600)
    OP_8C(0xC, 90, 400)
    OP_43(0xB, 0x1, 0x0, 0x6)
    Sleep(100)
    OP_43(0xC, 0x1, 0x0, 0x6)
    Sleep(200)
    OP_43(0xD, 0x1, 0x0, 0x6)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x6)
    WaitChrThread(0xE, 0x1)
    SetChrPos(0xB, -52060, 0, -95510, 135)
    SetChrPos(0xC, -49600, 0, -95370, 180)
    SetChrPos(0xD, -50540, 0, -96510, 0)
    SetChrPos(0xE, -50810, 0, -94450, 90)
    SetChrChipByIndex(0xB, 6)
    SetChrChipByIndex(0xC, 6)
    SetChrChipByIndex(0xD, 6)
    SetChrChipByIndex(0xE, 6)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    OP_6D(-50470, 0, -97380, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 16777215)
    OP_0D()
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_43(0x12A, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x146, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0x129, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x7)
    WaitChrThread(0x146, 0x1)

    ChrTalk(    #13
        0x146,
        "#6P#213FHoly crap! That was quick!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x129,
        "#192FAn S2 sleeping gas bomb, huh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12A, 0x102, 400)

    ChrTalk(    #15
        0x12A,
        (
            "#200F#6PThat took effect far faster than\x01",
            "any gas bomb I know of.\x02\x03",

            "You blend it yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1035F#5PI did.\x02\x03",

            "#1031FThe recipe's a trade secret, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x12A,
        "#206F#6PHmph.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x129,
        "#490FWhatever, eh? Let's keep moving.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1802)
    EventEnd(0x0)
    Return()

    # Function_5_742 end

    def Function_6_B69(): pass

    label("Function_6_B69")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 5)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 6)
    Return()

    # Function_6_B69 end

    def Function_7_B87(): pass

    label("Function_7_B87")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -51090, 0, -101180, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_BAE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BAE)
    OP_8E(0xFE, 0xFFFF36CA, 0x0, 0xFFFE7BF4, 0x7D0, 0x0)
    Return()

    # Function_7_B87 end

    def Function_8_BCF(): pass

    label("Function_8_BCF")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -51090, 0, -101180, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_BF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BF6)
    OP_8E(0xFE, 0xFFFF3B7A, 0x0, 0xFFFE7D2A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_8_BCF end

    def Function_9_C1E(): pass

    label("Function_9_C1E")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -51090, 0, -101180, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_C45():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C45)
    OP_8E(0xFE, 0xFFFF36AC, 0x0, 0xFFFE80FE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_9_C1E end

    def Function_10_C6D(): pass

    label("Function_10_C6D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -51090, 0, -101180, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_C94():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C94)
    OP_8E(0xFE, 0xFFFF3B52, 0x0, 0xFFFE81E4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_C6D end

    def Function_11_CBC(): pass

    label("Function_11_CBC")


    def lambda_CC2():
        OP_8F(0xFE, 0xFFFF30F8, 0x0, 0xFFFE8AAE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_CC2)
    Sleep(50)

    def lambda_CE2():
        OP_8F(0xFE, 0xFFFF4246, 0x0, 0xFFFE8B76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_CE2)
    Sleep(50)

    def lambda_D02():
        OP_8F(0xFE, 0xFFFF3B16, 0x0, 0xFFFE82F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_D02)
    Sleep(50)

    def lambda_D22():
        OP_8F(0xFE, 0xFFFF383C, 0x0, 0xFFFE9260, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_D22)
    Return()

    # Function_11_CBC end

    def Function_12_D38(): pass

    label("Function_12_D38")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0x9, 5360, 200, -92360, 192)
    SetChrPos(0x8, 4720, 200, -94810, 12)
    SetChrPos(0xA, 6630, 0, -93560, 270)
    SetChrPos(0xF, 5200, 850, -93300, 0)
    SetChrPos(0x10, 4760, 850, -94000, 0)
    OP_6D(5760, 0, -92560, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #19
        0x8,
        (
            "#151FHaaaaah... Such a wonderful meal.\x02\x03",

            "I'm moved to teeeears. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xA,
        (
            "Heh! Hearin' you say that makes\x01",
            "the work worth it, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "How about you, sir? Does it rate compared\x01",
            "to Erebonian cooking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "#277F#6POh, I'd rather say so, yes.\x02\x03",

            "It's like manna from heaven, compared to the\x01",
            "slop they feed us in the Imperial military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        "Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        (
            "What kind of food does the Erebonian army\x01",
            "prepare? If you, uh, can tell me, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#276F#6PHmm. Let's see...\x02\x03",

            "#272FCorned beef...that tastes of nothing but salt.\x02\x03",

            "Beans...so overcooked they have no texture.\x02\x03",

            "And bread that is more than a bit stale.\x02\x03",

            "#270FYou'll always find those three, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        "Ugh! I see what you mean, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#154FWow, that's awful!\x02\x03",

            "Is that why you guys attack people so often?\x01",
            "Because your food is yucky?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        "#276F#6PThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        "Ah, haha! C'mon, missy, don't be cruel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "#272F#6PWell, I'd certainly like to believe we're\x01",
            "not that kind of country.\x02\x03",

            "#270FStill, feeding a large army takes a great\x01",
            "deal of food, and serving low-quality food\x01",
            "allows it to be done more cheaply.\x02\x03",

            "That does factor into why the meals\x01",
            "served in our military are...lacking,\x01",
            "I imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "#153FWow... Sucks to be you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "Yeah. I'm glad things aren't like that\x01",
            "over here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C1305   ._SN", 133, 0, 0)
    IdleLoop()
    Return()

    # Function_12_D38 end

    SaveToFile()

Try(main)
