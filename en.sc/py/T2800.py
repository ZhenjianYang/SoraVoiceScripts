from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2800   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2800.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Reina',                                # 9
        'Bleublanc Ghost',                      # 10
        'Academy - Back Road',                  # 11
        'Vista Forest Rd',                      # 12
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
        'ED6_DT26/CH20273 ._CH',             # 00
        'ED6_DT07/CH01370 ._CH',             # 01
        'ED6_DT26/CH20276 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT26/CH20273P._CP',             # 00
        'ED6_DT07/CH01370P._CP',             # 01
        'ED6_DT26/CH20276P._CP',             # 02
    )

    DeclNpc(
        X                   = 31600,
        Z                   = 0,
        Y                   = 62470,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 84080,
        Z                   = 0,
        Y                   = 28010,
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
        X                   = -3490,
        Z                   = 0,
        Y                   = 46180,
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
        X                   = 41180,
        Y                   = 0,
        Z                   = 74060,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 67260,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 53150,
        Y                   = 0,
        Z                   = 59630,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 48380,
        Y                   = 0,
        Z                   = 45960,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 52870,
        Y                   = 0,
        Z                   = 32110,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 24850,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 47120,
        Y                   = 0,
        Z                   = 19010,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 22030,
        Y                   = 0,
        Z                   = 25660,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 22010,
        Y                   = 0,
        Z                   = 67170,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )


    DeclActor(
        TriggerX            = 65870,
        TriggerZ            = 0,
        TriggerY            = 27990,
        TriggerRange        = 800,
        ActorX              = 66000,
        ActorZ              = 1000,
        ActorY              = 28000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13480,
        TriggerZ            = 1000,
        TriggerY            = 46000,
        TriggerRange        = 1000,
        ActorX              = 13480,
        ActorZ              = 1000,
        ActorY              = 46000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2BE",          # 01, 1
        "Function_2_2F2",          # 02, 2
        "Function_3_308",          # 03, 3
        "Function_4_470",          # 04, 4
        "Function_5_6B4",          # 05, 5
        "Function_6_6CA",          # 06, 6
        "Function_7_82B",          # 07, 7
        "Function_8_87A",          # 08, 8
        "Function_9_87E",          # 09, 9
        "Function_10_882",         # 0A, 10
        "Function_11_886",         # 0B, 11
        "Function_12_88A",         # 0C, 12
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2BD")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_2BD")

    Return()

    # Function_0_2AA end

    def Function_1_2BE(): pass

    label("Function_1_2BE")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFEBFB0, 0x23004C)
    OP_72(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 3)), scpexpr(EXPR_END)), "loc_2EA")
    OP_64(0x0, 0x1)
    OP_6F(0xA, 60)
    Jump("loc_2F1")

    label("loc_2EA")

    OP_6F(0xA, 0)

    label("loc_2F1")

    Return()

    # Function_1_2BE end

    def Function_2_2F2(): pass

    label("Function_2_2F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2F2")

    label("loc_307")

    Return()

    # Function_2_2F2 end

    def Function_3_308(): pass

    label("Function_3_308")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3AC")

    ChrTalk(    #0
        0xFE,
        (
            "As you can see, I won't be able\x01",
            "to return to the dorm until her\x01",
            "anger has cooled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I suppose now is as good a time\x01",
            "as any to play my cards...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46C")

    label("loc_3AC")

    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        "Phew! Goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Felicity kicked me out of the room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I'd anticipated she would object,\x01",
            "but not to this extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I suppose now is as good a time\x01",
            "as any to play my cards...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C")

    TalkEnd(0xFE)
    Return()

    # Function_3_308 end

    def Function_4_470(): pass

    label("Function_4_470")

    EventBegin(0x0)
    ClearMapFlags(0x10)
    OP_6D(69000, 7000, 17030, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(286000, 0)
    OP_6E(439, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 71000, 7000, 17030, 180)

    def lambda_4D5():

        label("loc_4D5")

        OP_9E(0xFE, 0x0, 0xC8, 0x0, 0x1F4)
        OP_48()
        Jump("loc_4D5")

    QueueWorkItem2(0x9, 3, lambda_4D5)
    SetChrChipByIndex(0x9, 0)
    SetChrSubChip(0x9, 0)
    OP_43(0x9, 0x1, 0x1, 0x5)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    OP_A0(0x9, 0xB4, 0xB4, 0xB4, 0x0)
    FadeToBright(2000, 0)

    def lambda_521():
        OP_6B(2500, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_521)
    OP_97(0x9, 0x10D88, 0x4286, 0xFFFA81C0, 0xBB8, 0x1)
    OP_97(0x9, 0x10D88, 0x4286, 0xFFFA81C0, 0xBB8, 0x1)
    OP_97(0x9, 0x10D88, 0x4286, 0xFFFEA070, 0x7D0, 0x1)

    def lambda_570():
        OP_6D(60990, 4000, 17030, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_570)

    def lambda_588():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_588)

    def lambda_598():
        OP_6E(307, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_598)
    Sleep(300)
    OP_8C(0x9, 90, 1000)
    OP_8C(0x9, 360, 1000)
    OP_8C(0x9, 270, 1000)
    Sleep(300)
    Fade(500)

    def lambda_5CC():
        OP_96(0x9, 0xF60E, 0xFA0, 0x4286, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5CC)
    OP_0D()
    OP_44(0x9, 0x1)
    SetChrChipByIndex(0x9, 2)
    SetChrSubChip(0x9, 0)
    OP_43(0x9, 0x1, 0x1, 0x5)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x0, 0x3)
    Sleep(1000)
    OP_8C(0x9, 90, 1000)
    OP_8C(0x9, 360, 1000)
    OP_8C(0x9, 270, 1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "◆ブルブラン、優雅に一礼するＡＰＬ表示。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    OP_44(0x9, 0x1)
    SetChrChipByIndex(0x9, 0)
    SetChrSubChip(0x9, 0)
    OP_43(0x9, 0x1, 0x1, 0x5)

    def lambda_682():
        OP_8E(0xFE, 0x12110, 0x1B58, 0x4F4C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_682)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_470 end

    def Function_5_6B4(): pass

    label("Function_5_6B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C9")
    OP_99(0xFE, 0x0, 0x7, 0x1F4)
    Jump("Function_5_6B4")

    label("loc_6C9")

    Return()

    # Function_5_6B4 end

    def Function_6_6CA(): pass

    label("Function_6_6CA")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #7
        "\x07\x05The back gate is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Key]\x01",      # 0
            "[Don't]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_753"),
        (SWITCH_DEFAULT, "loc_81E"),
    )


    label("loc_753")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(64870, 0, 27950, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(105000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 64260, 0, 28070, 91)
    SetChrPos(0xF7, 63120, 0, 29050, 85)
    SetChrPos(0x105, 63880, 0, 27370, 105)
    SetChrPos(0x104, 62150, 0, 28600, 100)
    SetChrPos(0x127, 61540, 0, 27540, 74)
    OP_0D()
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    OP_71(0xA, 0x2)
    OP_73(0xA)
    OP_64(0x0, 0x1)
    OP_A2(0x1223)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_81E")

    label("loc_81E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_6_6CA end

    def Function_7_82B(): pass

    label("Function_7_82B")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        "\x07\x05The gate is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_82B end

    def Function_8_87A(): pass

    label("Function_8_87A")

    SetPlaceName(0x5F)
    Return()

    # Function_8_87A end

    def Function_9_87E(): pass

    label("Function_9_87E")

    SetPlaceName(0x5C)
    Return()

    # Function_9_87E end

    def Function_10_882(): pass

    label("Function_10_882")

    SetPlaceName(0x5D)
    Return()

    # Function_10_882 end

    def Function_11_886(): pass

    label("Function_11_886")

    SetPlaceName(0x6C)
    Return()

    # Function_11_886 end

    def Function_12_88A(): pass

    label("Function_12_88A")

    SetPlaceName(0x6D)
    Return()

    # Function_12_88A end

    SaveToFile()

Try(main)
