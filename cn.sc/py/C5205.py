from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5205   ._SN',
        MapName             = 'Other',
        Location            = 'C5205.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60063",
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
        '',                                     # 9
        '灰白神灵',                             # 10
        '地震控制用假人',                       # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12950 ._CH',             # 00
        'ED6_DT29/CH12951 ._CH',             # 01
        'ED6_DT29/CH12000 ._CH',             # 02
        'ED6_DT29/CH12001 ._CH',             # 03
        'ED6_DT29/CH12960 ._CH',             # 04
        'ED6_DT29/CH12961 ._CH',             # 05
        'ED6_DT29/CH13010 ._CH',             # 06
        'ED6_DT29/CH13011 ._CH',             # 07
        'ED6_DT29/CH12200 ._CH',             # 08
        'ED6_DT29/CH12201 ._CH',             # 09
        'ED6_DT29/CH13020 ._CH',             # 0A
        'ED6_DT29/CH13021 ._CH',             # 0B
        'ED6_DT29/CH13022 ._CH',             # 0C
        'ED6_DT27/CH04000 ._CH',             # 0D
        'ED6_DT27/CH04010 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT29/CH12950P._CP',             # 00
        'ED6_DT29/CH12951P._CP',             # 01
        'ED6_DT29/CH12000P._CP',             # 02
        'ED6_DT29/CH12001P._CP',             # 03
        'ED6_DT29/CH12960P._CP',             # 04
        'ED6_DT29/CH12961P._CP',             # 05
        'ED6_DT29/CH13010P._CP',             # 06
        'ED6_DT29/CH13011P._CP',             # 07
        'ED6_DT29/CH12200P._CP',             # 08
        'ED6_DT29/CH12201P._CP',             # 09
        'ED6_DT29/CH13020P._CP',             # 0A
        'ED6_DT29/CH13021P._CP',             # 0B
        'ED6_DT29/CH13022P._CP',             # 0C
        'ED6_DT27/CH04000P._CP',             # 0D
        'ED6_DT27/CH04010P._CP',             # 0E
    )

    DeclNpc(
        X                   = 25400,
        Z                   = 2000,
        Y                   = 264500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -494240,
        Z                   = 1000,
        Y                   = 349840,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -13960,
        Z                   = 0,
        Y                   = 232650,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x521,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 23950,
        Z                   = 0,
        Y                   = 246580,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x51E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -499610,
        Y                   = 0,
        Z                   = 338130,
        Range               = -487150,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x537DC,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 24790,
        TriggerZ            = 0,
        TriggerY            = 264470,
        TriggerRange        = 1000,
        ActorX              = 25400,
        ActorZ              = 0,
        ActorY              = 264500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19370,
        TriggerZ            = 0,
        TriggerY            = 264470,
        TriggerRange        = 1000,
        ActorX              = 20030,
        ActorZ              = 0,
        ActorY              = 264500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14260,
        TriggerZ            = 0,
        TriggerY            = 264510,
        TriggerRange        = 1000,
        ActorX              = 14880,
        ActorZ              = 0,
        ActorY              = 264540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9260,
        TriggerZ            = 0,
        TriggerY            = 264520,
        TriggerRange        = 1000,
        ActorX              = 9870,
        ActorZ              = 0,
        ActorY              = 264550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4140,
        TriggerZ            = 0,
        TriggerY            = 264520,
        TriggerRange        = 1000,
        ActorX              = 4790,
        ActorZ              = 0,
        ActorY              = 264500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -960,
        TriggerZ            = 0,
        TriggerY            = 264510,
        TriggerRange        = 1000,
        ActorX              = -320,
        ActorZ              = 0,
        ActorY              = 264540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6070,
        TriggerZ            = 0,
        TriggerY            = 264500,
        TriggerRange        = 1000,
        ActorX              = -5470,
        ActorZ              = 0,
        ActorY              = 264530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_300",          # 01, 1
        "Function_2_3DA",          # 02, 2
        "Function_3_3F0",          # 03, 3
        "Function_4_513",          # 04, 4
        "Function_5_792",          # 05, 5
        "Function_6_81F",          # 06, 6
        "Function_7_8F6",          # 07, 7
        "Function_8_9E1",          # 08, 8
        "Function_9_A0A",          # 09, 9
        "Function_10_BDA",         # 0A, 10
        "Function_11_CF1",         # 0B, 11
        "Function_12_E08",         # 0C, 12
        "Function_13_F1F",         # 0D, 13
        "Function_14_1036",        # 0E, 14
        "Function_15_114D",        # 0F, 15
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF")
    SetChrPos(0x9, -493940, 1000, 344240, 180)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)

    label("loc_2FF")

    Return()

    # Function_0_2D6 end

    def Function_1_300(): pass

    label("Function_1_300")

    Call(0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_32A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x42), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_43(0xA, 0x3, 0x0, 0x8)
    OP_22(0x85, 0x1, 0x46)

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C")
    OP_6F(0x6, 0)
    Jump("loc_343")

    label("loc_33C")

    OP_6F(0x6, 60)

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355")
    OP_6F(0x7, 0)
    Jump("loc_35C")

    label("loc_355")

    OP_6F(0x7, 60)

    label("loc_35C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E")
    OP_6F(0x8, 0)
    Jump("loc_375")

    label("loc_36E")

    OP_6F(0x8, 60)

    label("loc_375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_387")
    OP_6F(0x9, 0)
    Jump("loc_38E")

    label("loc_387")

    OP_6F(0x9, 60)

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0")
    OP_6F(0xA, 0)
    Jump("loc_3A7")

    label("loc_3A0")

    OP_6F(0xA, 60)

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9")
    OP_6F(0xB, 0)
    Jump("loc_3C0")

    label("loc_3B9")

    OP_6F(0xB, 60)

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D2")
    OP_6F(0xC, 0)
    Jump("loc_3D9")

    label("loc_3D2")

    OP_6F(0xC, 60)

    label("loc_3D9")

    Return()

    # Function_1_300 end

    def Function_2_3DA(): pass

    label("Function_2_3DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3DA")

    label("loc_3EF")

    Return()

    # Function_2_3DA end

    def Function_3_3F0(): pass

    label("Function_3_3F0")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_419"),
        (3, "loc_426"),
        (4, "loc_433"),
        (5, "loc_440"),
        (6, "loc_44D"),
        (7, "loc_45A"),
        (8, "loc_467"),
        (10, "loc_474"),
        (SWITCH_DEFAULT, "loc_481"),
    )


    label("loc_419")

    OP_D2(0x701D0, 0x701DC, 0xF)
    Jump("loc_481")

    label("loc_426")

    OP_D2(0x701E8, 0x701F4, 0xF)
    Jump("loc_481")

    label("loc_433")

    OP_D2(0x27036E, 0x27037B, 0xF)
    Jump("loc_481")

    label("loc_440")

    OP_D2(0x70218, 0x70224, 0xF)
    Jump("loc_481")

    label("loc_44D")

    OP_D2(0x70230, 0x7023C, 0xF)
    Jump("loc_481")

    label("loc_45A")

    OP_D2(0x70248, 0x70254, 0xF)
    Jump("loc_481")

    label("loc_467")

    OP_D2(0x270176, 0x270183, 0xF)
    Jump("loc_481")

    label("loc_474")

    OP_D2(0x702B4, 0x702BB, 0xF)
    Jump("loc_481")

    label("loc_481")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_4AA"),
        (3, "loc_4B7"),
        (4, "loc_4C4"),
        (5, "loc_4D1"),
        (6, "loc_4DE"),
        (7, "loc_4EB"),
        (8, "loc_4F8"),
        (10, "loc_505"),
        (SWITCH_DEFAULT, "loc_512"),
    )


    label("loc_4AA")

    OP_D2(0x701D0, 0x701DC, 0x10)
    Jump("loc_512")

    label("loc_4B7")

    OP_D2(0x701E8, 0x701F4, 0x10)
    Jump("loc_512")

    label("loc_4C4")

    OP_D2(0x27036E, 0x27037B, 0x10)
    Jump("loc_512")

    label("loc_4D1")

    OP_D2(0x70218, 0x70224, 0x10)
    Jump("loc_512")

    label("loc_4DE")

    OP_D2(0x70230, 0x7023C, 0x10)
    Jump("loc_512")

    label("loc_4EB")

    OP_D2(0x70248, 0x70254, 0x10)
    Jump("loc_512")

    label("loc_4F8")

    OP_D2(0x270176, 0x270183, 0x10)
    Jump("loc_512")

    label("loc_505")

    OP_D2(0x702B4, 0x702BB, 0x10)
    Jump("loc_512")

    label("loc_512")

    Return()

    # Function_3_3F0 end

    def Function_4_513(): pass

    label("Function_4_513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 5)), scpexpr(EXPR_END)), "loc_51B")
    Return()

    label("loc_51B")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-495000, 0, 344000, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    SetChrPos(0x9, -494240, 3000, 349840, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x20)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 12)
    SetChrSubChip(0x9, 5)
    SetChrPos(0x101, -494200, 0, 340900, 0)
    SetChrPos(0x102, -495070, 0, 340030, 0)
    SetChrPos(0xF8, -493940, 0, 338820, 0)
    SetChrPos(0xF9, -492910, 0, 339230, 0)

    def lambda_5D9():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D9)

    def lambda_5F4():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F4)

    def lambda_60F():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_60F)

    def lambda_62A():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_62A)

    def lambda_645():
        OP_6D(-495000, 0, 348000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_645)
    OP_0D()

    def lambda_65E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_65E)

    def lambda_670():
        OP_8F(0xFE, 0xFFF87560, 0x3E8, 0x55690, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_670)
    OP_43(0x9, 0x0, 0x0, 0x5)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 14)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 15)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0xF9, 0)
    WaitChrThread(0x9, 0x0)
    Sleep(400)

    def lambda_739():
        OP_99(0xFE, 0x5, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_739)
    WaitChrThread(0x9, 0x3)

    def lambda_74E():
        OP_99(0xFE, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_74E)
    Sleep(500)
    Battle(0x523, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_77E"),
        (0, "loc_783"),
        (2, "loc_78A"),
        (SWITCH_DEFAULT, "loc_791"),
    )


    label("loc_77E")

    OP_B4(0x0)
    Jump("loc_791")

    label("loc_783")

    Call(0, 6)
    Jump("loc_791")

    label("loc_78A")

    Call(0, 7)
    Jump("loc_791")

    label("loc_791")

    Return()

    # Function_4_513 end

    def Function_5_792(): pass

    label("Function_5_792")

    OP_8C(0xFE, 90, 800)
    OP_8C(0xFE, 0, 800)
    OP_8C(0xFE, 270, 800)
    OP_8C(0xFE, 180, 800)
    OP_8C(0xFE, 90, 800)
    OP_8C(0xFE, 0, 800)
    OP_8C(0xFE, 270, 800)
    OP_8C(0xFE, 180, 800)
    OP_8C(0xFE, 90, 800)
    OP_8C(0xFE, 0, 800)
    OP_8C(0xFE, 270, 800)
    OP_8C(0xFE, 180, 800)
    OP_8C(0xFE, 90, 800)
    OP_8C(0xFE, 0, 800)
    OP_8C(0xFE, 270, 800)
    OP_8C(0xFE, 180, 800)
    OP_8C(0xFE, 90, 800)
    OP_8C(0xFE, 0, 800)
    OP_8C(0xFE, 270, 800)
    OP_8C(0xFE, 180, 800)
    Return()

    # Function_5_792 end

    def Function_6_81F(): pass

    label("Function_6_81F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    OP_6D(-494000, 0, 340660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -494000, 0, 340660, 0)
    SetChrPos(0x1, -494000, 0, 340660, 0)
    SetChrPos(0x2, -494000, 0, 340660, 0)
    SetChrPos(0x3, -494000, 0, 340660, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x22FD)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_81F end

    def Function_7_8F6(): pass

    label("Function_7_8F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x9, 0x1)
    SetChrPos(0x9, -493940, 3000, 344240, 180)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_6D(-494000, 0, 336660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -494000, 0, 336660, 180)
    SetChrPos(0x1, -494000, 0, 336660, 180)
    SetChrPos(0x2, -494000, 0, 336660, 180)
    SetChrPos(0x3, -494000, 0, 336660, 180)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_8F6 end

    def Function_8_9E1(): pass

    label("Function_8_9E1")

    OP_C4(0x0, 0x20)

    label("loc_9E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A09")
    OP_7C(0x3C, 0x3C, 0x3E8, 0x384)
    Sleep(1000)
    Jump("loc_9E7")

    label("loc_A09")

    Return()

    # Function_8_9E1 end

    def Function_9_A0A(): pass

    label("Function_9_A0A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE9")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_A5C():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A5C)

    def lambda_A77():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A77)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x522, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_AC4"),
        (2, "loc_AD6"),
        (1, "loc_AE6"),
        (SWITCH_DEFAULT, "loc_AE9"),
    )


    label("loc_AC4")

    OP_A2(0x234B)
    OP_6F(0x6, 60)
    Sleep(500)
    Jump("loc_AE9")

    label("loc_AD6")

    OP_6F(0x6, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_AE6")

    OP_B4(0x0)
    Return()

    label("loc_AE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18A, 1)"), scpexpr(EXPR_END)), "loc_B38")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\x8A\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x234A)
    Jump("loc_B9A")

    label("loc_B38")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\x8A\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x8A\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_B9A")

    Jump("loc_BCC")

    label("loc_B9D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BCC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_A0A end

    def Function_10_BDA(): pass

    label("Function_10_BDA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_C49")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x234C)
    Jump("loc_CAF")

    label("loc_C49")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_CAF")

    Jump("loc_CE3")

    label("loc_CB2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CE3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_BDA end

    def Function_11_CF1(): pass

    label("Function_11_CF1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_D60")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x234D)
    Jump("loc_DC6")

    label("loc_D60")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_DC6")

    Jump("loc_DFA")

    label("loc_DC9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DFA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_CF1 end

    def Function_12_E08(): pass

    label("Function_12_E08")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x140, 1)"), scpexpr(EXPR_END)), "loc_E77")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\x40\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x234E)
    Jump("loc_EDD")

    label("loc_E77")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "宝箱里装有\x1F\x40\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x40\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_EDD")

    Jump("loc_F11")

    label("loc_EE0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F11")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_E08 end

    def Function_13_F1F(): pass

    label("Function_13_F1F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x469, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_F8E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x234F)
    Jump("loc_FF4")

    label("loc_F8E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_FF4")

    Jump("loc_1028")

    label("loc_FF7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1028")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_F1F end

    def Function_14_1036(): pass

    label("Function_14_1036")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_10A5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2350)
    Jump("loc_110B")

    label("loc_10A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x06\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_110B")

    Jump("loc_113F")

    label("loc_110E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_113F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1036 end

    def Function_15_114D(): pass

    label("Function_15_114D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1225")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x295, 1)"), scpexpr(EXPR_END)), "loc_11BC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\x95\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2351)
    Jump("loc_1222")

    label("loc_11BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "宝箱里装有\x1F\x95\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x95\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_1222")

    Jump("loc_1256")

    label("loc_1225")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1256")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_114D end

    SaveToFile()

Try(main)
