from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5700   ._SN',
        MapName             = 'Other',
        Location            = 'C5700.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        '工业区域『法克特里亚』2',              # 9
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
        'ED6_DT29/CH12060 ._CH',             # 00
        'ED6_DT29/CH12061 ._CH',             # 01
        'ED6_DT29/CH12190 ._CH',             # 02
        'ED6_DT29/CH12191 ._CH',             # 03
        'ED6_DT29/CH12970 ._CH',             # 04
        'ED6_DT29/CH12971 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH12060P._CP',             # 00
        'ED6_DT29/CH12061P._CP',             # 01
        'ED6_DT29/CH12190P._CP',             # 02
        'ED6_DT29/CH12191P._CP',             # 03
        'ED6_DT29/CH12970P._CP',             # 04
        'ED6_DT29/CH12971P._CP',             # 05
    )

    DeclNpc(
        X                   = -1870,
        Z                   = 4000,
        Y                   = 70500,
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


    DeclMonster(
        X                   = -1660,
        Z                   = 4000,
        Y                   = -82810,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x514,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2200,
        Z                   = 4000,
        Y                   = -35950,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x515,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2080,
        Z                   = 4000,
        Y                   = 6660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x514,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33090,
        Z                   = 4000,
        Y                   = -85830,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x515,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -63370,
        Z                   = 4000,
        Y                   = -95010,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -65340,
        Z                   = 4000,
        Y                   = -75570,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23570,
        Z                   = 4000,
        Y                   = 39810,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23470,
        Z                   = 4000,
        Y                   = -28170,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 54520,
        Z                   = 4000,
        Y                   = -15020,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 42010,
        Z                   = 4250,
        Y                   = 48860,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x516,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -35030,
        TriggerZ            = 4000,
        TriggerY            = 5960,
        TriggerRange        = 5000,
        ActorX              = -31230,
        ActorZ              = 5500,
        ActorY              = 5960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -72130,
        TriggerZ            = 4000,
        TriggerY            = -77200,
        TriggerRange        = 1000,
        ActorX              = -71520,
        ActorZ              = 4000,
        ActorY              = -77200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41290,
        TriggerZ            = 4250,
        TriggerY            = -37040,
        TriggerRange        = 1000,
        ActorX              = 41910,
        ActorZ              = 4250,
        ActorY              = -37040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 55710,
        TriggerZ            = 4000,
        TriggerY            = 72760,
        TriggerRange        = 1000,
        ActorX              = 55970,
        ActorZ              = 4000,
        ActorY              = 73340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A2",          # 00, 0
        "Function_1_2D2",          # 01, 1
        "Function_2_33A",          # 02, 2
        "Function_3_451",          # 03, 3
        "Function_4_568",          # 04, 4
        "Function_5_664",          # 05, 5
        "Function_6_6D8",          # 06, 6
        "Function_7_F72",          # 07, 7
        "Function_8_FB1",          # 08, 8
        "Function_9_FF7",          # 09, 9
        "Function_10_103D",        # 0A, 10
        "Function_11_1068",        # 0B, 11
        "Function_12_10EF",        # 0C, 12
        "Function_13_1182",        # 0D, 13
    )


    def Function_0_2A2(): pass

    label("Function_0_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2B3")
    OP_A3(0x10F0)
    Event(0, 5)
    Jump("loc_2D1")

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D1")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_2D1")

    Return()

    # Function_0_2A2 end

    def Function_1_2D2(): pass

    label("Function_1_2D2")

    OP_16(0x2, 0xFA0, 0xFFFE36F8, 0xFFFDC998, 0x230074)
    OP_22(0x1C7, 0x0, 0x64)
    OP_71(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300")
    OP_6F(0x7, 0)
    Jump("loc_307")

    label("loc_300")

    OP_6F(0x7, 60)

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319")
    OP_6F(0x8, 0)
    Jump("loc_320")

    label("loc_319")

    OP_6F(0x8, 60)

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_332")
    OP_6F(0x9, 0)
    Jump("loc_339")

    label("loc_332")

    OP_6F(0x9, 60)

    label("loc_339")

    Return()

    # Function_1_2D2 end

    def Function_2_33A(): pass

    label("Function_2_33A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_412")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xC3, 1)"), scpexpr(EXPR_END)), "loc_3A9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xC3\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2320)
    Jump("loc_40F")

    label("loc_3A9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xC3\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xC3\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_40F")

    Jump("loc_443")

    label("loc_412")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_443")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_33A end

    def Function_3_451(): pass

    label("Function_3_451")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A1, 1)"), scpexpr(EXPR_END)), "loc_4C0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xA1\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2321)
    Jump("loc_526")

    label("loc_4C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xA1\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xA1\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_526")

    Jump("loc_55A")

    label("loc_529")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_55A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_451 end

    def Function_4_568(): pass

    label("Function_4_568")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x464, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_638")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x1E)
    OP_73(0x9)
    OP_6F(0x9, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2322)
    Jump("loc_652")

    label("loc_638")


    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_652")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_568 end

    def Function_5_664(): pass

    label("Function_5_664")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(40820, 4350, -31840, 0)
    OP_67(0, 7210, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(339000, 0)
    OP_6E(890, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(2000)
    OP_22(0x7C, 0x0, 0x64)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_664 end

    def Function_6_6D8(): pass

    label("Function_6_6D8")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EF")
    Call(0, 11)
    Call(0, 12)

    label("loc_6EF")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-3530, 4350, -118640, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3730, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)

    def lambda_761():
        OP_6D(-2020, 4000, -124090, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_761)
    OP_43(0x101, 0x1, 0x0, 0x7)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x8)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #8
        0x101,
        "#1004F#6P这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#1044F好宽阔的地方啊……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_11(0xAA, 0xC8, 0xFF, 0x0, 0x61A80, 0x0)
    OP_6D(-2020, 4000, -124090, 0)
    OP_67(0, 12070, -10000, 0)
    OP_6B(6250, 0)
    OP_6C(321000, 0)
    OP_6E(439, 0)

    def lambda_837():
        OP_6D(50600, 4000, -6600, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_837)

    def lambda_84F():
        OP_67(0, 8940, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84F)

    def lambda_867():
        OP_6B(12250, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_867)

    def lambda_877():
        OP_6C(338000, 12000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_877)

    def lambda_887():
        OP_6E(600, 12000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_887)
    OP_C8(0x200, 0x46, "C_PLAC27._CH", 0x0, 0xFA0)
    Sleep(2000)

    def lambda_8B1():
        OP_8E(0xFE, 0x137E, 0xFA0, 0xFFFE2988, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_8B1)
    Sleep(800)

    def lambda_8D1():
        OP_8E(0xFE, 0x184C, 0xFA0, 0xFFFE292E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8D1)
    Sleep(800)

    def lambda_8F1():
        OP_8E(0xFE, 0x1338, 0xFA0, 0xFFFE247E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_8F1)
    Sleep(800)

    def lambda_911():
        OP_8E(0xFE, 0x1A68, 0xFA0, 0xFFFE233E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_911)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_6F(0x0, 0)
    OP_11(0xAA, 0xC8, 0xFF, 0x124F8, 0x186A0, 0x0)
    OP_6D(4980, 4000, -120120, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(3860, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x101, 6250, 4000, -120500, 0)
    SetChrPos(0x102, 4950, 4000, -120500, 0)
    SetChrPos(0xF8, 6250, 4000, -121800, 0)
    SetChrPos(0xF9, 4950, 4000, -121800, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A42")

    ChrTalk(    #10
        0x102,
        (
            "#1044F#5P……放眼望去，\x01",
            "到处都林立着巨大的建筑物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04")

    label("loc_A42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8F")

    ChrTalk(    #11
        0x109,
        (
            "#1064F#6P这真是，放眼望去\x01",
            "到处都林立着巨大的建筑物啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04")

    label("loc_A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD9")

    ChrTalk(    #12
        0x103,
        (
            "#023F#6P……放眼望去，\x01",
            "到处都林立着巨大的建筑物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04")

    label("loc_AD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B23")

    ChrTalk(    #13
        0x106,
        (
            "#052F#6P……放眼望去，\x01",
            "到处都林立着巨大的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04")

    label("loc_B23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6D")

    ChrTalk(    #14
        0x108,
        (
            "#073F#6P……放眼望去，\x01",
            "到处都林立着巨大的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04")

    label("loc_B6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB7")

    ChrTalk(    #15
        0x104,
        (
            "#033F#6P呵，放眼望去，\x01",
            "到处都林立着巨大的建筑物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04")

    label("loc_BB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C04")

    ChrTalk(    #16
        0x10B,
        (
            "#213F#6P这真是，放眼望去，\x01",
            "到处都林立着巨大的建筑物呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4F")

    ChrTalk(    #17
        0x105,
        (
            "#1163F#6P道路也相当宽敞……\x01",
            "究竟是个什么样的地方呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBA")

    label("loc_C4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C97")

    ChrTalk(    #18
        0x10B,
        (
            "#212F#6P道路也很宽阔……\x01",
            "究竟是个什么样的地方呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBA")

    label("loc_C97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE1")

    ChrTalk(    #19
        0x104,
        (
            "#035F#6P嗯，道路也很宽阔，\x01",
            "究竟是个什么样的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBA")

    label("loc_CE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2B")

    ChrTalk(    #20
        0x108,
        (
            "#073F#6P道路也相当宽阔……\x01",
            "究竟是个什么样的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBA")

    label("loc_D2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D75")

    ChrTalk(    #21
        0x106,
        (
            "#555F#6P道路也相当宽阔……\x01",
            "究竟是个什么样的地方啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBA")

    label("loc_D75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBA")

    ChrTalk(    #22
        0x103,
        (
            "#022F#6P道路也很宽阔……\x01",
            "究竟是个什么样的地方呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EAF")

    ChrTalk(    #23
        0x107,
        (
            "#560F#6P或许……\x01",
            "这里是工业区域也说不定。\x02\x03",

            "如果将大量的水想成是工业用水，\x01",
            "感觉上就很吻合了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1040F#5P原来如此，说得过去呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1016F#5P的确，作为居住区的话，\x01",
            "气氛就不那么安定了。\x02\x03",

            "#1006F……好。\x01",
            "马上开始探索吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F62")

    label("loc_EAF")


    ChrTalk(    #26
        0x102,
        (
            "#1035F#5P……或许\x01",
            "这里是工业区域也说不定。\x02\x03",

            "#1040F如果将大量的水想成是工业用水，\x01",
            "不就说得过去了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1015F#5P原来如此，的确有这可能啊。\x02\x03",

            "#1006F……好。\x01",
            "马上开始探索吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F62")

    OP_A2(0x221E)
    OP_28(0x9E, 0x4, 0x2)
    OP_28(0x9E, 0x4, 0x8)
    EventEnd(0x0)
    Return()

    # Function_6_6D8 end

    def Function_7_F72(): pass

    label("Function_7_F72")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2120, 4350, -118450, 180)
    OP_8E(0xFE, 0xFFFFF7C2, 0xFA0, 0xFFFE1F38, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7FE, 0xFA0, 0xFFFE16B4, 0x7D0, 0x0)
    Return()

    # Function_7_F72 end

    def Function_8_FB1(): pass

    label("Function_8_FB1")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2120, 4350, -118450, 180)
    OP_8E(0xFE, 0xFFFFF7C2, 0xFA0, 0xFFFE1F38, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFC68, 0xFA0, 0xFFFE1B1E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_FB1 end

    def Function_9_FF7(): pass

    label("Function_9_FF7")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2120, 4350, -118450, 180)
    OP_8E(0xFE, 0xFFFFF7C2, 0xFA0, 0xFFFE1F38, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF3E4, 0xFA0, 0xFFFE1BFA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_9_FF7 end

    def Function_10_103D(): pass

    label("Function_10_103D")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2120, 4350, -118450, 180)
    OP_8E(0xFE, 0xFFFFF7C2, 0xFA0, 0xFFFE1F38, 0x7D0, 0x0)
    Return()

    # Function_10_103D end

    def Function_11_1068(): pass

    label("Function_11_1068")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10E2"),
        (1, "loc_10E8"),
        (SWITCH_DEFAULT, "loc_10EE"),
    )


    label("loc_10E2")

    OP_A2(0x1200)
    Jump("loc_10EE")

    label("loc_10E8")

    OP_A2(0x1201)
    Jump("loc_10EE")

    label("loc_10EE")

    Return()

    # Function_11_1068 end

    def Function_12_10EF(): pass

    label("Function_12_10EF")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_12_10EF end

    def Function_13_1182(): pass

    label("Function_13_1182")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #28
        "\x07\x05门牢牢地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1182 end

    SaveToFile()

Try(main)
