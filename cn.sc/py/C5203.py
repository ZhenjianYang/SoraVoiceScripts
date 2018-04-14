from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5203   ._SN',
        MapName             = 'Other',
        Location            = 'C5203.x',
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
        '雷电漂浮鱼',                           # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH13012 ._CH',             # 0A
        'ED6_DT27/CH04000 ._CH',             # 0B
        'ED6_DT27/CH04010 ._CH',             # 0C
        'ED6_DT07/CH00120 ._CH',             # 0D
        'ED6_DT07/CH00130 ._CH',             # 0E
        'ED6_DT27/CH04210 ._CH',             # 0F
        'ED6_DT07/CH00150 ._CH',             # 10
        'ED6_DT07/CH00160 ._CH',             # 11
        'ED6_DT07/CH00170 ._CH',             # 12
        'ED6_DT27/CH04080 ._CH',             # 13
        'ED6_DT07/CH00310 ._CH',             # 14
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
        'ED6_DT29/CH13012P._CP',             # 0A
        'ED6_DT27/CH04000P._CP',             # 0B
        'ED6_DT27/CH04010P._CP',             # 0C
        'ED6_DT07/CH00120P._CP',             # 0D
        'ED6_DT07/CH00130P._CP',             # 0E
        'ED6_DT27/CH04210P._CP',             # 0F
        'ED6_DT07/CH00150P._CP',             # 10
        'ED6_DT07/CH00160P._CP',             # 11
        'ED6_DT07/CH00170P._CP',             # 12
        'ED6_DT27/CH04080P._CP',             # 13
        'ED6_DT07/CH00310P._CP',             # 14
    )

    DeclNpc(
        X                   = 215200,
        Z                   = 3000,
        Y                   = 742660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 102030,
        Z                   = 0,
        Y                   = 442060,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x444,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 129440,
        Z                   = 0,
        Y                   = 527920,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x440,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 205850,
        Z                   = -8000,
        Y                   = 536430,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x441,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 199590,
        Z                   = -4000,
        Y                   = 514909,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x444,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 192670,
        Z                   = 4000,
        Y                   = 550140,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x440,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 215040,
        Z                   = 0,
        Y                   = 625890,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x444,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 207310,
        Y                   = 0,
        Z                   = 725940,
        Range               = 221440,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xB1FBC,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 309300,
        TriggerZ            = 0,
        TriggerY            = 524000,
        TriggerRange        = 1000,
        ActorX              = 309910,
        ActorZ              = 0,
        ActorY              = 524000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 309300,
        TriggerZ            = 0,
        TriggerY            = 464000,
        TriggerRange        = 1000,
        ActorX              = 310000,
        ActorZ              = 0,
        ActorY              = 464000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 207370,
        TriggerZ            = 0,
        TriggerY            = 550010,
        TriggerRange        = 1000,
        ActorX              = 208030,
        ActorZ              = 0,
        ActorY              = 550010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 220660,
        TriggerZ            = 0,
        TriggerY            = 550040,
        TriggerRange        = 1000,
        ActorX              = 220000,
        ActorZ              = 0,
        ActorY              = 549950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2CA",          # 00, 0
        "Function_1_2E9",          # 01, 1
        "Function_2_352",          # 02, 2
        "Function_3_368",          # 03, 3
        "Function_4_48B",          # 04, 4
        "Function_5_6FC",          # 05, 5
        "Function_6_7D3",          # 06, 6
        "Function_7_8B3",          # 07, 7
        "Function_8_9CA",          # 08, 8
        "Function_9_AE1",          # 09, 9
        "Function_10_BF8",         # 0A, 10
    )


    def Function_0_2CA(): pass

    label("Function_0_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E8")
    SetChrPos(0x8, 215200, 3000, 742660, 180)
    ClearChrFlags(0x8, 0x80)

    label("loc_2E8")

    Return()

    # Function_0_2CA end

    def Function_1_2E9(): pass

    label("Function_1_2E9")

    Call(0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x463, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF")
    OP_6F(0x9, 0)
    Jump("loc_306")

    label("loc_2FF")

    OP_6F(0x9, 60)

    label("loc_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x463, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318")
    OP_6F(0xA, 0)
    Jump("loc_31F")

    label("loc_318")

    OP_6F(0xA, 60)

    label("loc_31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x463, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331")
    OP_6F(0xB, 0)
    Jump("loc_338")

    label("loc_331")

    OP_6F(0xB, 60)

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x463, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A")
    OP_6F(0xC, 0)
    Jump("loc_351")

    label("loc_34A")

    OP_6F(0xC, 60)

    label("loc_351")

    Return()

    # Function_1_2E9 end

    def Function_2_352(): pass

    label("Function_2_352")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_367")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_352")

    label("loc_367")

    Return()

    # Function_2_352 end

    def Function_3_368(): pass

    label("Function_3_368")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_391"),
        (3, "loc_39E"),
        (4, "loc_3AB"),
        (5, "loc_3B8"),
        (6, "loc_3C5"),
        (7, "loc_3D2"),
        (8, "loc_3DF"),
        (10, "loc_3EC"),
        (SWITCH_DEFAULT, "loc_3F9"),
    )


    label("loc_391")

    OP_D2(0x701D0, 0x701DC, 0xD)
    Jump("loc_3F9")

    label("loc_39E")

    OP_D2(0x701E8, 0x701F4, 0xD)
    Jump("loc_3F9")

    label("loc_3AB")

    OP_D2(0x27036E, 0x27037B, 0xD)
    Jump("loc_3F9")

    label("loc_3B8")

    OP_D2(0x70218, 0x70224, 0xD)
    Jump("loc_3F9")

    label("loc_3C5")

    OP_D2(0x70230, 0x7023C, 0xD)
    Jump("loc_3F9")

    label("loc_3D2")

    OP_D2(0x70248, 0x70254, 0xD)
    Jump("loc_3F9")

    label("loc_3DF")

    OP_D2(0x270176, 0x270183, 0xD)
    Jump("loc_3F9")

    label("loc_3EC")

    OP_D2(0x702B4, 0x702BB, 0xD)
    Jump("loc_3F9")

    label("loc_3F9")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_422"),
        (3, "loc_42F"),
        (4, "loc_43C"),
        (5, "loc_449"),
        (6, "loc_456"),
        (7, "loc_463"),
        (8, "loc_470"),
        (10, "loc_47D"),
        (SWITCH_DEFAULT, "loc_48A"),
    )


    label("loc_422")

    OP_D2(0x701D0, 0x701DC, 0xE)
    Jump("loc_48A")

    label("loc_42F")

    OP_D2(0x701E8, 0x701F4, 0xE)
    Jump("loc_48A")

    label("loc_43C")

    OP_D2(0x27036E, 0x27037B, 0xE)
    Jump("loc_48A")

    label("loc_449")

    OP_D2(0x70218, 0x70224, 0xE)
    Jump("loc_48A")

    label("loc_456")

    OP_D2(0x70230, 0x7023C, 0xE)
    Jump("loc_48A")

    label("loc_463")

    OP_D2(0x70248, 0x70254, 0xE)
    Jump("loc_48A")

    label("loc_470")

    OP_D2(0x270176, 0x270183, 0xE)
    Jump("loc_48A")

    label("loc_47D")

    OP_D2(0x702B4, 0x702BB, 0xE)
    Jump("loc_48A")

    label("loc_48A")

    Return()

    # Function_3_368 end

    def Function_4_48B(): pass

    label("Function_4_48B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45F, 6)), scpexpr(EXPR_END)), "loc_493")
    Return()

    label("loc_493")

    EventBegin(0x0)
    Fade(500)
    OP_6D(214520, 0, 729820, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 215200, 3000, 742660, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x20)
    OP_43(0x8, 0x0, 0x0, 0x2)

    def lambda_4FF():
        OP_8F(0xFE, 0x348A0, 0x0, 0xB3D94, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4FF)
    SetChrPos(0x101, 214970, 0, 726800, 0)
    SetChrPos(0x102, 214100, 0, 725930, 0)
    SetChrPos(0xF8, 215230, 0, 724720, 0)
    SetChrPos(0xF9, 216260, 0, 725130, 0)

    def lambda_55E():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55E)

    def lambda_579():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_579)

    def lambda_594():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_594)

    def lambda_5AF():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5AF)

    def lambda_5CA():
        OP_6D(214520, 0, 734820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CA)
    OP_0D()
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
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 11)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 12)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 13)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 14)
    SetChrSubChip(0xF9, 0)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 0)

    def lambda_69D():
        OP_99(0xFE, 0x0, 0x7, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_69D)

    def lambda_6AD():
        OP_8F(0xFE, 0x34C88, 0x0, 0xB1710, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6AD)
    Sleep(300)
    Battle(0x446, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_6E8"),
        (0, "loc_6ED"),
        (2, "loc_6F4"),
        (SWITCH_DEFAULT, "loc_6FB"),
    )


    label("loc_6E8")

    OP_B4(0x0)
    Jump("loc_6FB")

    label("loc_6ED")

    Call(0, 5)
    Jump("loc_6FB")

    label("loc_6F4")

    Call(0, 6)
    Jump("loc_6FB")

    label("loc_6FB")

    Return()

    # Function_4_48B end

    def Function_5_6FC(): pass

    label("Function_5_6FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    OP_6D(214940, 0, 728800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 214940, 0, 728800, 0)
    SetChrPos(0x1, 214940, 0, 728800, 0)
    SetChrPos(0x2, 214940, 0, 728800, 0)
    SetChrPos(0x3, 214940, 0, 728800, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_A2(0x22FE)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_6FC end

    def Function_6_7D3(): pass

    label("Function_6_7D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x8, 0x1)
    SetChrPos(0x8, 215200, 3000, 742660, 180)
    ClearChrFlags(0x8, 0x80)
    OP_6D(214940, 0, 723800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 214940, 0, 723800, 180)
    SetChrPos(0x1, 214940, 0, 723800, 180)
    SetChrPos(0x2, 214940, 0, 723800, 180)
    SetChrPos(0x3, 214940, 0, 723800, 180)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_7D3 end

    def Function_7_8B3(): pass

    label("Function_7_8B3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x463, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x189, 1)"), scpexpr(EXPR_END)), "loc_922")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x89\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2318)
    Jump("loc_988")

    label("loc_922")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x89\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x89\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_988")

    Jump("loc_9BC")

    label("loc_98B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9BC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_8B3 end

    def Function_8_9CA(): pass

    label("Function_8_9CA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x463, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xA6, 1)"), scpexpr(EXPR_END)), "loc_A39")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xA6\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x231A)
    Jump("loc_A9F")

    label("loc_A39")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xA6\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xA6\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_A9F")

    Jump("loc_AD3")

    label("loc_AA2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AD3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_9CA end

    def Function_9_AE1(): pass

    label("Function_9_AE1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x463, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_B50")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x231C)
    Jump("loc_BB6")

    label("loc_B50")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_BB6")

    Jump("loc_BEA")

    label("loc_BB9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BEA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_AE1 end

    def Function_10_BF8(): pass

    label("Function_10_BF8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x463, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A3, 1)"), scpexpr(EXPR_END)), "loc_C67")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xA3\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x231D)
    Jump("loc_CCD")

    label("loc_C67")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xA3\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xA3\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_CCD")

    Jump("loc_D01")

    label("loc_CD0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D01")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_BF8 end

    SaveToFile()

Try(main)
