from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7101   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60222",
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
        '死亡迷幻华劣克',                       # 9
        '钢鳞恶魔',                             # 10
        '钢鳞恶魔',                             # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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


    AddCharChip(
        'ED6_DT29/CH14070 ._CH',             # 00
        'ED6_DT29/CH14071 ._CH',             # 01
        'ED6_DT29/CH14830 ._CH',             # 02
        'ED6_DT29/CH14831 ._CH',             # 03
        'ED6_DT29/CH14910 ._CH',             # 04
        'ED6_DT29/CH14911 ._CH',             # 05
        'ED6_DT29/CH14920 ._CH',             # 06
        'ED6_DT29/CH14921 ._CH',             # 07
        'ED6_DT29/CH14930 ._CH',             # 08
        'ED6_DT29/CH14931 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14070P._CP',             # 00
        'ED6_DT29/CH14071P._CP',             # 01
        'ED6_DT29/CH14830P._CP',             # 02
        'ED6_DT29/CH14831P._CP',             # 03
        'ED6_DT29/CH14910P._CP',             # 04
        'ED6_DT29/CH14911P._CP',             # 05
        'ED6_DT29/CH14920P._CP',             # 06
        'ED6_DT29/CH14921P._CP',             # 07
        'ED6_DT29/CH14930P._CP',             # 08
        'ED6_DT29/CH14931P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 37630,
        Z                   = -10000,
        Y                   = -86120,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x136,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 72130,
        Z                   = -14000,
        Y                   = -86130,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x135,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 72230,
        Z                   = -18000,
        Y                   = -43980,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x134,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 72090,
        Z                   = -18000,
        Y                   = 3960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x137,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37880,
        Z                   = -22000,
        Y                   = -44070,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x138,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -44240,
        Z                   = -34000,
        Y                   = -44080,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x136,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25290,
        Z                   = -34000,
        Y                   = 20840,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x138,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8780,
        Z                   = -38000,
        Y                   = 50930,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x137,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 42560,
        Z                   = -42000,
        Y                   = 20950,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x135,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -17190,
        TriggerZ            = -38000,
        TriggerY            = 53290,
        TriggerRange        = 1000,
        ActorX              = -17000,
        ActorZ              = -35000,
        ActorY              = 55000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22000,
        TriggerZ            = -6000,
        TriggerY            = -86000,
        TriggerRange        = 1000,
        ActorX              = -22000,
        ActorZ              = -5000,
        ActorY              = -86000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 96000,
        TriggerZ            = -18000,
        TriggerY            = 4000,
        TriggerRange        = 1000,
        ActorX              = 96000,
        ActorZ              = -17000,
        ActorY              = 4000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 69000,
        TriggerZ            = -42000,
        TriggerY            = 21000,
        TriggerRange        = 1000,
        ActorX              = 69000,
        ActorZ              = -41000,
        ActorY              = 21000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14000,
        TriggerZ            = -30000,
        TriggerY            = -44000,
        TriggerRange        = 1000,
        ActorX              = -14000,
        ActorZ              = -29000,
        ActorY              = -44000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -44000,
        TriggerZ            = -34000,
        TriggerY            = -12000,
        TriggerRange        = 1000,
        ActorX              = -44000,
        ActorZ              = -33000,
        ActorY              = -12000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 96000,
        TriggerZ            = -18000,
        TriggerY            = 7000,
        TriggerRange        = 1000,
        ActorX              = 96000,
        ActorZ              = -17000,
        ActorY              = 7000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 96000,
        TriggerZ            = -18000,
        TriggerY            = 1000,
        TriggerRange        = 1000,
        ActorX              = 96000,
        ActorZ              = -17000,
        ActorY              = 1000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72000,
        TriggerZ            = -18000,
        TriggerY            = -18000,
        TriggerRange        = 1000,
        ActorX              = 72000,
        ActorZ              = -17000,
        ActorY              = -18000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 42800,
        TriggerZ            = -38000,
        TriggerY            = 83000,
        TriggerRange        = 1000,
        ActorX              = 42800,
        ActorZ              = -37000,
        ActorY              = 83000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3BE",          # 00, 0
        "Function_1_410",          # 01, 1
        "Function_2_54A",          # 02, 2
        "Function_3_553",          # 03, 3
        "Function_4_D83",          # 04, 4
        "Function_5_134D",         # 05, 5
        "Function_6_13B5",         # 06, 6
        "Function_7_141D",         # 07, 7
        "Function_8_1485",         # 08, 8
        "Function_9_14B1",         # 09, 9
        "Function_10_14E2",        # 0A, 10
        "Function_11_1513",        # 0B, 11
        "Function_12_1544",        # 0C, 12
        "Function_13_1622",        # 0D, 13
        "Function_14_16DE",        # 0E, 14
        "Function_15_17F4",        # 0F, 15
        "Function_16_1842",        # 10, 16
        "Function_17_18B6",        # 11, 17
        "Function_18_1A7B",        # 12, 18
        "Function_19_1B31",        # 13, 19
        "Function_20_1BDC",        # 14, 20
        "Function_21_1CFC",        # 15, 21
        "Function_22_1E1C",        # 16, 22
        "Function_23_1E99",        # 17, 23
        "Function_24_1FB9",        # 18, 24
        "Function_25_2036",        # 19, 25
        "Function_26_2156",        # 1A, 26
        "Function_27_2276",        # 1B, 27
        "Function_28_2396",        # 1C, 28
    )


    def Function_0_3BE(): pass

    label("Function_0_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3D4")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_3F0")

    label("loc_3D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3F0")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_3F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_408"),
        (SWITCH_DEFAULT, "loc_40F"),
    )


    label("loc_408")

    Event(0, 12)
    Jump("loc_40F")

    label("loc_40F")

    Return()

    # Function_0_3BE end

    def Function_1_410(): pass

    label("Function_1_410")

    OP_16(0x2, 0xFA0, 0xFFFE6DA8, 0xFFFDCD80, 0x230084)
    OP_1B(0x1, 0x0, 0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43F")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_10(0x0, 0x0)
    Jump("loc_452")

    label("loc_43F")

    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 120)
    OP_72(0x800, 0x0)
    ExitThread()

    label("loc_452")

    OP_82(0x82, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_465")
    OP_82(0x83, 0x0)
    Jump("loc_468")

    label("loc_465")

    OP_82(0x84, 0x0)

    label("loc_468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A")
    OP_6F(0x2, 0)
    Jump("loc_481")

    label("loc_47A")

    OP_6F(0x2, 60)

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493")
    OP_6F(0x3, 0)
    Jump("loc_49A")

    label("loc_493")

    OP_6F(0x3, 60)

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC")
    OP_6F(0x4, 0)
    Jump("loc_4B3")

    label("loc_4AC")

    OP_6F(0x4, 60)

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C5")
    OP_6F(0x5, 0)
    Jump("loc_4CC")

    label("loc_4C5")

    OP_6F(0x5, 60)

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE")
    OP_6F(0x6, 0)
    Jump("loc_4E5")

    label("loc_4DE")

    OP_6F(0x6, 60)

    label("loc_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F7")
    OP_6F(0x7, 0)
    Jump("loc_4FE")

    label("loc_4F7")

    OP_6F(0x7, 60)

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_510")
    OP_6F(0x8, 0)
    Jump("loc_517")

    label("loc_510")

    OP_6F(0x8, 60)

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529")
    OP_6F(0x9, 0)
    Jump("loc_530")

    label("loc_529")

    OP_6F(0x9, 60)

    label("loc_530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_542")
    OP_6F(0xA, 0)
    Jump("loc_549")

    label("loc_542")

    OP_6F(0xA, 60)

    label("loc_549")

    Return()

    # Function_1_410 end

    def Function_2_54A(): pass

    label("Function_2_54A")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_54A end

    def Function_3_553(): pass

    label("Function_3_553")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_AA(65282)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    OP_E0(242, 0x4A, 0x2)
    OP_E0(243, 0x4B, 0x2)
    OP_E0(244, 0x4C, 0x2)
    OP_E0(245, 0x4D, 0x2)
    SetChrPos(0xF2, 8050, -6000, -110050, 0)
    SetChrPos(0xF3, 8600, -6000, -110510, 0)
    SetChrPos(0xF4, 7540, -6000, -110380, 0)
    SetChrPos(0xF5, 8150, -6000, -110780, 0)
    OP_9F(0xF2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6F(0x0, 120)
    OP_6D(11020, -4750, -109000, 0)
    OP_67(0, 6440, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(140000, 0)
    OP_6E(243, 0)

    def lambda_658():
        OP_6B(4500, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_658)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0xF2, 0x0, 0x0, 0x8)
    OP_43(0xF3, 0x0, 0x0, 0x9)
    OP_43(0xF4, 0x0, 0x0, 0xA)
    OP_43(0xF5, 0x0, 0x0, 0xB)
    Sleep(2000)
    OP_22(0x6C, 0x0, 0x64)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 120)
    OP_70(0x0, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(3780, -8700, -97230, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(28000, 0)
    OP_6E(480, 0)

    def lambda_6F1():
        OP_6D(3780, -2000, -95500, 7000)
        ExitThread()

    QueueWorkItem(0xF2, 2, lambda_6F1)

    def lambda_709():
        OP_67(0, 4600, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xF2, 3, lambda_709)

    def lambda_721():
        OP_6B(5680, 7000)
        ExitThread()

    QueueWorkItem(0xF3, 2, lambda_721)

    def lambda_731():
        OP_6C(28000, 7000)
        ExitThread()

    QueueWorkItem(0xF4, 3, lambda_731)

    def lambda_741():
        OP_6E(492, 7000)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_741)
    StopSound(0x20B70, 0x5BCC0, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC33._CH", 0x0, 0x3E8)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    WaitChrThread(0xF2, 0x2)
    Fade(500)
    OP_6D(8660, -6000, -87180, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)
    StopSound(0xEE48, 0x33450, 0x0)
    OP_0D()
    Sleep(300)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 7900, -5900, -83150, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 3600, -5900, -85600, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 11840, -5900, -85910, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B3")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_91A")

    label("loc_8B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DB")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_91A")

    label("loc_8DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_903")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_91A")

    label("loc_903")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_91A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_947")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9AE")

    label("loc_947")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96F")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9AE")

    label("loc_96F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_997")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9AE")

    label("loc_997")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9AE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DB")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A42")

    label("loc_9DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A03")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A42")

    label("loc_A03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2B")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A42")

    label("loc_A2B")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A42")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6F")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AD6")

    label("loc_A6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A97")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AD6")

    label("loc_A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABF")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AD6")

    label("loc_ABF")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_AD6")

    Sleep(1000)
    OP_1D(0x97)

    ChrTalk(    #0
        0x10F,
        "#1443F#6P啊……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B31")

    ChrTalk(    #1
        0x10D,
        "#270F#6P……来了吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_B31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B65")

    ChrTalk(    #2
        0x10E,
        "#172F#6P这么突然……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_B65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9A")

    ChrTalk(    #3
        0x102,
        "#1502F#6P……来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_B9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCD")

    ChrTalk(    #4
        0x105,
        "#1162F#6P……哼………\x02",
    )

    CloseMessageWindow()
    Jump("loc_C00")

    label("loc_BCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C00")

    ChrTalk(    #5
        0x10B,
        "#216F#6P慢、慢着……！？\x02",
    )

    CloseMessageWindow()

    label("loc_C00")

    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 10)
    SetChrSubChip(0x10F, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF3, 11)
    SetChrSubChip(0xF3, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF4, 12)
    SetChrSubChip(0xF4, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF5, 13)
    SetChrSubChip(0xF5, 0)
    OP_0D()
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 7900, -8000, -83150, 180)
    SetChrPos(0x11, 3600, -8000, -85600, 135)
    SetChrPos(0x12, 11840, -8000, -85910, 225)
    OP_22(0x85, 0x1, 0x64)
    OP_43(0x10, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0x11, 0x0, 0x0, 0x6)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x7)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_23(0x85)
    Sleep(1000)

    def lambda_CE7():
        OP_6D(8580, -6000, -87820, 300)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_CE7)

    def lambda_CFF():
        OP_67(0, 7120, -10000, 300)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_CFF)

    def lambda_D17():
        OP_6B(2400, 300)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_D17)
    SetChrChipByIndex(0x11, 3)

    def lambda_D2C():
        OP_8F(0xFE, 0x19AA, 0xFFFFE890, 0xFFFEA692, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D2C)
    Sleep(50)
    SetChrChipByIndex(0x12, 3)

    def lambda_D51():
        OP_8F(0xFE, 0x2530, 0xFFFFE890, 0xFFFEA4F8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_D51)
    WaitChrThread(0x10F, 0x1)
    WaitChrThread(0x10F, 0x2)
    WaitChrThread(0x10F, 0x3)
    Battle(0x13F, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_553 end

    def Function_4_D83(): pass

    label("Function_4_D83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_E0(242, 0x4A, 0x2)
    OP_E0(243, 0x4B, 0x2)
    OP_E0(244, 0x4C, 0x2)
    OP_E0(245, 0x4D, 0x2)
    SetChrPos(0xF2, 7980, -6000, -89550, 0)
    SetChrPos(0xF3, 9030, -6000, -90970, 0)
    SetChrPos(0xF4, 6690, -6000, -91250, 0)
    SetChrPos(0xF5, 7930, -6000, -92360, 0)
    SetChrChipByIndex(0x10F, 10)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0xF3, 11)
    SetChrSubChip(0xF3, 0)
    SetChrChipByIndex(0xF4, 12)
    SetChrSubChip(0xF4, 0)
    SetChrChipByIndex(0xF5, 13)
    SetChrSubChip(0xF5, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Sleep(1000)
    OP_6D(8230, -6000, -84930, 0)
    OP_67(0, 7570, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(309, 0)

    def lambda_E7C():
        OP_6D(8660, -6000, -89910, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_E7C)

    def lambda_E94():
        OP_67(0, 6730, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_E94)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x10F,
        "#1445F#5P………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9E")
    OP_A2(0x0)

    ChrTalk(    #7
        0x107,
        (
            "#065F#6P刚、刚才的……\x02\x03",

            "简直和童话故事里\x01",
            "出现过的死神一样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1155")

    label("loc_F9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1007")
    OP_A2(0x3)

    ChrTalk(    #8
        0x10B,
        (
            "#216F#6P什么呀，那东西……\x02\x03",

            "简直和童话故事里\x01",
            "出现过的死神一样！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1155")

    label("loc_1007")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1079")
    OP_A2(0x5)

    ChrTalk(    #9
        0x105,
        (
            "#1163F#6P刚、刚才的怪物……\x02\x03",

            "简直给人以童话故事里\x01",
            "出现过的死神那样的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1155")

    label("loc_1079")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E7")
    OP_A2(0x4)

    ChrTalk(    #10
        0x102,
        (
            "#1502F#6P刚才的怪物……\x02\x03",

            "简直给人以童话故事里\x01",
            "出现过的死神那样的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1155")

    label("loc_10E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1155")
    OP_A2(0x1)

    ChrTalk(    #11
        0x10E,
        (
            "#178F#6P……方才的怪物………\x02\x03",

            "其气息简直和民间故事里\x01",
            "出现过的死神一样……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1155")

    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #12
        0x10F,
        (
            "#1446F#5P……嗯嗯，的确。\x02\x03",

            "#1443F与恶魔一样是『不可能存在』的魔物，\x01",
            "但其意义又有所不同。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1228")

    ChrTalk(    #13
        0x105,
        (
            "#1167F#6P……看起来，\x01",
            "敌人不会让我们这么轻易就到达终点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132C")

    label("loc_1228")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1280")

    ChrTalk(    #14
        0x10E,
        (
            "#176F#6P……看起来，\x01",
            "要到终点非要花上一定的时间不可。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132C")

    label("loc_1280")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12D7")

    ChrTalk(    #15
        0x102,
        (
            "#1505F#6P……看起来，\x01",
            "要到终点也不是一件容易的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132C")

    label("loc_12D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132C")

    ChrTalk(    #16
        0x10B,
        (
            "#413F#6P唉……看起来，\x01",
            "要到终点也不是一件容易的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132C")

    OP_A2(0x2808)
    OP_28(0x31, 0x4, 0x4)
    OP_28(0x31, 0x4, 0x8)
    OP_28(0x31, 0x1, 0x1)
    OP_28(0x31, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_D83 end

    def Function_5_134D(): pass

    label("Function_5_134D")

    PlayEffect(0x1, 0x4, 0xFF, 7900, -5900, -83150, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_1388():

        label("loc_1388")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1388")

    QueueWorkItem2(0xFE, 1, lambda_1388)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_134D end

    def Function_6_13B5(): pass

    label("Function_6_13B5")

    PlayEffect(0x1, 0x5, 0xFF, 3600, -5900, -85600, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_13F0():

        label("loc_13F0")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13F0")

    QueueWorkItem2(0xFE, 1, lambda_13F0)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_13B5 end

    def Function_7_141D(): pass

    label("Function_7_141D")

    PlayEffect(0x1, 0x6, 0xFF, 11840, -5900, -85910, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_1458():

        label("loc_1458")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1458")

    QueueWorkItem2(0xFE, 1, lambda_1458)
    OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x6, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_141D end

    def Function_8_1485(): pass

    label("Function_8_1485")


    def lambda_148B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_148B)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x1F2C, 0xFFFFE890, 0xFFFEA232, 0x1388, 0x0)
    Return()

    # Function_8_1485 end

    def Function_9_14B1(): pass

    label("Function_9_14B1")

    Sleep(300)

    def lambda_14BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14BC)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x240E, 0xFFFFE890, 0xFFFE9D6E, 0x1388, 0x0)
    Return()

    # Function_9_14B1 end

    def Function_10_14E2(): pass

    label("Function_10_14E2")

    Sleep(600)

    def lambda_14ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14ED)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x1A22, 0xFFFFE890, 0xFFFE9BF2, 0x1388, 0x0)
    Return()

    # Function_10_14E2 end

    def Function_11_1513(): pass

    label("Function_11_1513")

    Sleep(1000)

    def lambda_151E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_151E)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x1EFA, 0xFFFFE890, 0xFFFE9738, 0x1388, 0x0)
    Return()

    # Function_11_1513 end

    def Function_12_1544(): pass

    label("Function_12_1544")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 42790, -37710, 74890, 180)
    SetChrPos(0x1, 42790, -37710, 74890, 180)
    SetChrPos(0x2, 42790, -37710, 74890, 180)
    SetChrPos(0x3, 42790, -37710, 74890, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 42790, -37710, 74890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 14)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_12_1544 end

    def Function_13_1622(): pass

    label("Function_13_1622")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x0, 42790, -37710, 74890, 0)
    SetChrPos(0x1, 42790, -37710, 74890, 0)
    SetChrPos(0x2, 42790, -37710, 74890, 0)
    SetChrPos(0x3, 42790, -37710, 74890, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 42790, -37710, 74890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 15)
    NewScene("ED6_DT21/M7103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1622 end

    def Function_14_16DE(): pass

    label("Function_14_16DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1707")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_16FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_16FB)

    label("loc_1707")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1730")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1724():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1724)

    label("loc_1730")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1759")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_174D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_174D)

    label("loc_1759")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1782")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1776():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1776)

    label("loc_1782")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17AE")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_17AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C5")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_17C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17DC")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_17DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F3")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_17F3")

    Return()

    # Function_14_16DE end

    def Function_15_17F4(): pass

    label("Function_15_17F4")


    def lambda_17FA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_17FA)

    def lambda_180C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_180C)

    def lambda_181E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_181E)

    def lambda_1830():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1830)
    Sleep(1000)
    Return()

    # Function_15_17F4 end

    def Function_16_1842(): pass

    label("Function_16_1842")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_189F")

    label("loc_189F")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_16_1842 end

    def Function_17_18B6(): pass

    label("Function_17_18B6")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -16250, -38000, 52300, 0)
    SetChrPos(0x1, -17950, -38000, 52240, 0)
    SetChrPos(0x2, -16580, -38000, 50060, 0)
    SetChrPos(0x3, -18080, -38000, 50420, 0)
    OP_6D(-17350, -38000, 53300, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(4630, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198C")
    OP_28(0x5, 0x4, 0x2)
    OP_82(0x83, 0x2)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_198C")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x05#40W　汝须将蕴藏纯白光辉之少女，\x01",
            "　   携学生之『证』\x01",
            "　　 引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A6F")
    Call(0, 16)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6C")
    Call(0, 18)

    label("loc_1A6C")

    Jump("loc_1A6F")

    label("loc_1A6F")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_17_18B6 end

    def Function_18_1A7B(): pass

    label("Function_18_1A7B")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)

    def lambda_1AE4():
        OP_6B(4100, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1AE4)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x8, 0, 0x0)
    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1A7B end

    def Function_19_1B31(): pass

    label("Function_19_1B31")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -16250, -38000, 52300, 0)
    SetChrPos(0x1, -17950, -38000, 52240, 0)
    SetChrPos(0x2, -16580, -38000, 50060, 0)
    SetChrPos(0x3, -18080, -38000, 50420, 0)
    OP_6D(-17350, -38000, 53300, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(4630, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_19_1B31 end

    def Function_20_1BDC(): pass

    label("Function_20_1BDC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CBD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_1C4E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    Jump("loc_1C33")

    label("loc_1C33")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2890)
    Jump("loc_1CBA")

    label("loc_1C4E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x02\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1C9B")

    label("loc_1C9B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1CBA")

    Jump("loc_1CEE")

    label("loc_1CBD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1CEE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_20_1BDC end

    def Function_21_1CFC(): pass

    label("Function_21_1CFC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25A, 1)"), scpexpr(EXPR_END)), "loc_1D6E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\x5A\x02\x07\x00。\x02",
    )

    Jump("loc_1D53")

    label("loc_1D53")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2891)
    Jump("loc_1DDA")

    label("loc_1D6E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "宝箱里装有\x1F\x5A\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x5A\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1DBB")

    label("loc_1DBB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1DDA")

    Jump("loc_1E0E")

    label("loc_1DDD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1E0E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_21_1CFC end

    def Function_22_1E1C(): pass

    label("Function_22_1E1C")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 26)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2892)
    Jump("loc_1E87")

    label("loc_1E6D")


    AnonymousTalk(    #25
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1E87")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_22_1E1C end

    def Function_23_1E99(): pass

    label("Function_23_1E99")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1F0B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    Jump("loc_1EF0")

    label("loc_1EF0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2893)
    Jump("loc_1F77")

    label("loc_1F0B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1F58")

    label("loc_1F58")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_1F77")

    Jump("loc_1FAB")

    label("loc_1F7A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1FAB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_23_1E99 end

    def Function_24_1FB9(): pass

    label("Function_24_1FB9")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x1E)
    OP_73(0x6)
    OP_6F(0x6, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 26)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2894)
    Jump("loc_2024")

    label("loc_200A")


    AnonymousTalk(    #29
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2024")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_24_1FB9 end

    def Function_25_2036(): pass

    label("Function_25_2036")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2117")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1B4, 1)"), scpexpr(EXPR_END)), "loc_20A8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x00得到了\x1F\xB4\x01\x07\x00。\x02",
    )

    Jump("loc_208D")

    label("loc_208D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2895)
    Jump("loc_2114")

    label("loc_20A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "宝箱里装有\x1F\xB4\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xB4\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_20F5")

    label("loc_20F5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_2114")

    Jump("loc_2148")

    label("loc_2117")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2148")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_25_2036 end

    def Function_26_2156(): pass

    label("Function_26_2156")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2237")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x192, 1)"), scpexpr(EXPR_END)), "loc_21C8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x00得到了\x1F\x92\x01\x07\x00。\x02",
    )

    Jump("loc_21AD")

    label("loc_21AD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2896)
    Jump("loc_2234")

    label("loc_21C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "宝箱里装有\x1F\x92\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x92\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2215")

    label("loc_2215")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_2234")

    Jump("loc_2268")

    label("loc_2237")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2268")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_26_2156 end

    def Function_27_2276(): pass

    label("Function_27_2276")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x512, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2357")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x69, 1)"), scpexpr(EXPR_END)), "loc_22E8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        "\x07\x00得到了\x1F\x69\x00\x07\x00。\x02",
    )

    Jump("loc_22CD")

    label("loc_22CD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2897)
    Jump("loc_2354")

    label("loc_22E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "宝箱里装有\x1F\x69\x00\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x69\x00\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2335")

    label("loc_2335")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_2354")

    Jump("loc_2388")

    label("loc_2357")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2388")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_27_2276 end

    def Function_28_2396(): pass

    label("Function_28_2396")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x515, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2477")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x170, 1)"), scpexpr(EXPR_END)), "loc_2408")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x00得到了\x1F\x70\x01\x07\x00。\x02",
    )

    Jump("loc_23ED")

    label("loc_23ED")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28AB)
    Jump("loc_2474")

    label("loc_2408")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "宝箱里装有\x1F\x70\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x70\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2455")

    label("loc_2455")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_2474")

    Jump("loc_24A8")

    label("loc_2477")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_24A8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_28_2396 end

    SaveToFile()

Try(main)
