from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5317   ._SN',
        MapName             = 'Other',
        Location            = 'C5317.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C5317   ._SN',
            'ED6_DT21/C5317_1 ._SN',
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
        'Weissmann',                            # 9
        'Loewe',                                # 10
        'Major Vander',                         # 11
        'Captain Schwarz',                      # 12
        'Professor Russell',                    # 13
        'Don',                                  # 14
        'Kyle',                                 # 15
        'Estelle',                              # 16
        'Joshua',                               # 17
        '非パーティメンバー',                   # 18
        '非パーティメンバー',                   # 19
        '非パーティメンバー',                   # 20
        '非パーティメンバー',                   # 21
        '非パーティメンバー',                   # 22
        '非パーティメンバー',                   # 23
        'Kloe',                                 # 24
        'Scherazard',                           # 25
        '戦術殻',                               # 26
        '戦術殻',                               # 27
        '戦術殻',                               # 28
        '戦術殻',                               # 29
        '残像',                                 # 30
        'ターゲット',                           # 31
        'ターゲット',                           # 32
        'Dragion',                              # 33
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C0,
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
        NpcIndex            = 0x1C0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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


    ScpFunction(
        "Function_0_3CA",          # 00, 0
        "Function_1_3F2",          # 01, 1
        "Function_2_471",          # 02, 2
        "Function_3_754",          # 03, 3
        "Function_4_AB0",          # 04, 4
        "Function_5_DB1",          # 05, 5
        "Function_6_1204",         # 06, 6
        "Function_7_1219",         # 07, 7
        "Function_8_605B",         # 08, 8
        "Function_9_92A2",         # 09, 9
        "Function_10_A836",        # 0A, 10
        "Function_11_CFDE",        # 0B, 11
        "Function_12_D006",        # 0C, 12
        "Function_13_D073",        # 0D, 13
        "Function_14_D0D0",        # 0E, 14
        "Function_15_D149",        # 0F, 15
        "Function_16_D190",        # 10, 16
        "Function_17_D20C",        # 11, 17
        "Function_18_D288",        # 12, 18
        "Function_19_D2CF",        # 13, 19
        "Function_20_D304",        # 14, 20
        "Function_21_D392",        # 15, 21
        "Function_22_D420",        # 16, 22
        "Function_23_D4AE",        # 17, 23
        "Function_24_D53C",        # 18, 24
        "Function_25_D5CB",        # 19, 25
        "Function_26_D660",        # 1A, 26
        "Function_27_D6F5",        # 1B, 27
        "Function_28_D78A",        # 1C, 28
        "Function_29_D81F",        # 1D, 29
        "Function_30_D8B4",        # 1E, 30
        "Function_31_D957",        # 1F, 31
        "Function_32_D9A4",        # 20, 32
        "Function_33_D9E9",        # 21, 33
        "Function_34_DA6F",        # 22, 34
    )


    def Function_0_3CA(): pass

    label("Function_0_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3E4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(1, 2)
    Jump("loc_3F1")

    label("loc_3E4")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x41), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)

    label("loc_3F1")

    Return()

    # Function_0_3CA end

    def Function_1_3F2(): pass

    label("Function_1_3F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2714), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_407")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x459), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x22DA)

    label("loc_41F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x465), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x22DA)

    label("loc_437")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x451), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x38), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x22DB)

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_45F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45F")

    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    Return()

    # Function_1_3F2 end

    def Function_2_471(): pass

    label("Function_2_471")

    OP_D2(0x270132, 0x270142, 0x0)
    OP_D2(0x270132, 0x270142, 0x1)
    OP_D2(0x27027E, 0x270288, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x270111, 0x270121, 0x4)
    OP_D2(0x270114, 0x270124, 0x5)
    OP_D2(0x270130, 0x270140, 0x6)
    OP_D2(0x270131, 0x270141, 0x7)
    OP_D2(0x270132, 0x270142, 0x8)
    OP_D2(0x270134, 0x270144, 0x9)
    OP_D2(0x270139, 0x270149, 0xA)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_510"),
        (5, "loc_527"),
        (3, "loc_53E"),
        (4, "loc_555"),
        (6, "loc_56C"),
        (7, "loc_583"),
        (8, "loc_59A"),
        (10, "loc_5B1"),
        (14, "loc_5C8"),
        (15, "loc_5DF"),
        (SWITCH_DEFAULT, "loc_5F6"),
    )


    label("loc_510")

    OP_D2(0x701D0, 0x701DC, 0xB)
    OP_D2(0x701D1, 0x701DD, 0xC)
    Jump("loc_5F6")

    label("loc_527")

    OP_D2(0x70218, 0x70224, 0xB)
    OP_D2(0x70219, 0x70225, 0xC)
    Jump("loc_5F6")

    label("loc_53E")

    OP_D2(0x701E8, 0x701F4, 0xB)
    OP_D2(0x701E9, 0x701F5, 0xC)
    Jump("loc_5F6")

    label("loc_555")

    OP_D2(0x27036E, 0x27037B, 0xB)
    OP_D2(0x27036F, 0x27037C, 0xC)
    Jump("loc_5F6")

    label("loc_56C")

    OP_D2(0x70230, 0x7023C, 0xB)
    OP_D2(0x70231, 0x7023D, 0xC)
    Jump("loc_5F6")

    label("loc_583")

    OP_D2(0x70248, 0x70254, 0xB)
    OP_D2(0x70249, 0x70255, 0xC)
    Jump("loc_5F6")

    label("loc_59A")

    OP_D2(0x270176, 0x270183, 0xB)
    OP_D2(0x270177, 0x270184, 0xC)
    Jump("loc_5F6")

    label("loc_5B1")

    OP_D2(0x702B4, 0x702BB, 0xB)
    OP_D2(0x702B5, 0x702BC, 0xC)
    Jump("loc_5F6")

    label("loc_5C8")

    OP_D2(0x2702D6, 0x2702E0, 0xB)
    OP_D2(0x2702D7, 0x2702E1, 0xC)
    Jump("loc_5F6")

    label("loc_5DF")

    OP_D2(0x2702C2, 0x2702CC, 0xB)
    OP_D2(0x2702C3, 0x2702CD, 0xC)
    Jump("loc_5F6")

    label("loc_5F6")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_627"),
        (5, "loc_63E"),
        (3, "loc_655"),
        (4, "loc_66C"),
        (6, "loc_683"),
        (7, "loc_69A"),
        (8, "loc_6B1"),
        (10, "loc_6C8"),
        (14, "loc_6DF"),
        (15, "loc_6EC"),
        (SWITCH_DEFAULT, "loc_6F9"),
    )


    label("loc_627")

    OP_D2(0x701D0, 0x701DC, 0xD)
    OP_D2(0x701D1, 0x701DD, 0xE)
    Jump("loc_6F9")

    label("loc_63E")

    OP_D2(0x70218, 0x70224, 0xD)
    OP_D2(0x70219, 0x70225, 0xE)
    Jump("loc_6F9")

    label("loc_655")

    OP_D2(0x701E8, 0x701F4, 0xD)
    OP_D2(0x701E9, 0x701F5, 0xE)
    Jump("loc_6F9")

    label("loc_66C")

    OP_D2(0x27036E, 0x27037B, 0xD)
    OP_D2(0x27036F, 0x27037C, 0xE)
    Jump("loc_6F9")

    label("loc_683")

    OP_D2(0x70230, 0x7023C, 0xD)
    OP_D2(0x70231, 0x7023D, 0xE)
    Jump("loc_6F9")

    label("loc_69A")

    OP_D2(0x70248, 0x70254, 0xD)
    OP_D2(0x70249, 0x70255, 0xE)
    Jump("loc_6F9")

    label("loc_6B1")

    OP_D2(0x270176, 0x270183, 0xD)
    OP_D2(0x270177, 0x270184, 0xE)
    Jump("loc_6F9")

    label("loc_6C8")

    OP_D2(0x702B4, 0x702BB, 0xD)
    OP_D2(0x702B5, 0x702BC, 0xE)
    Jump("loc_6F9")

    label("loc_6DF")

    OP_D2(0x2702D6, 0x2702E0, 0xD)
    Jump("loc_6F9")

    label("loc_6EC")

    OP_D2(0x2702C2, 0x2702CC, 0xD)
    Jump("loc_6F9")

    label("loc_6F9")

    OP_D2(0x27028E, 0x270298, 0xF)
    OP_D2(0x27028F, 0x270299, 0x10)
    OP_D2(0x270290, 0x27029A, 0x11)
    OP_D2(0x270293, 0x27029D, 0x12)
    OP_D2(0x270296, 0x2702A0, 0x13)
    OP_D2(0x29021E, 0x290222, 0x14)
    OP_D2(0x26022C, 0x26022F, 0x15)
    OP_D2(0x2601F9, 0x2601FE, 0x16)
    OP_D2(0x27027C, 0x270286, 0x17)
    Return()

    # Function_2_471 end

    def Function_3_754(): pass

    label("Function_3_754")

    OP_C0(0x10, 0x6, 0xFF, 0x7, 0x8, 0xA, 0xFF, 0xB, 0xC)
    AddParty(0x1, 0xF7, 0xFF)
    OP_D2(0x270132, 0x270142, 0x0)
    OP_D2(0x2601E5, 0x2601EA, 0x1)
    OP_D2(0x27027E, 0x270288, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x270111, 0x270121, 0x4)
    OP_D2(0x270114, 0x270124, 0x5)
    OP_D2(0x270130, 0x270140, 0x6)
    OP_D2(0x270131, 0x270141, 0x7)
    OP_D2(0x270132, 0x270142, 0x8)
    OP_D2(0x270134, 0x270144, 0x9)
    OP_D2(0x270139, 0x270149, 0xA)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_819"),
        (5, "loc_830"),
        (3, "loc_847"),
        (4, "loc_85E"),
        (6, "loc_875"),
        (7, "loc_88C"),
        (8, "loc_8A3"),
        (10, "loc_8BA"),
        (14, "loc_8D1"),
        (15, "loc_8E8"),
        (SWITCH_DEFAULT, "loc_8FF"),
    )


    label("loc_819")

    OP_D2(0x701D0, 0x701DC, 0xB)
    OP_D2(0x701D1, 0x701DD, 0xC)
    Jump("loc_8FF")

    label("loc_830")

    OP_D2(0x70218, 0x70224, 0xB)
    OP_D2(0x70219, 0x70225, 0xC)
    Jump("loc_8FF")

    label("loc_847")

    OP_D2(0x701E8, 0x701F4, 0xB)
    OP_D2(0x701E9, 0x701F5, 0xC)
    Jump("loc_8FF")

    label("loc_85E")

    OP_D2(0x27036E, 0x27037B, 0xB)
    OP_D2(0x27036F, 0x27037C, 0xC)
    Jump("loc_8FF")

    label("loc_875")

    OP_D2(0x70230, 0x7023C, 0xB)
    OP_D2(0x70231, 0x7023D, 0xC)
    Jump("loc_8FF")

    label("loc_88C")

    OP_D2(0x70248, 0x70254, 0xB)
    OP_D2(0x70249, 0x70255, 0xC)
    Jump("loc_8FF")

    label("loc_8A3")

    OP_D2(0x270176, 0x270183, 0xB)
    OP_D2(0x270177, 0x270184, 0xC)
    Jump("loc_8FF")

    label("loc_8BA")

    OP_D2(0x702B4, 0x702BB, 0xB)
    OP_D2(0x702B5, 0x702BC, 0xC)
    Jump("loc_8FF")

    label("loc_8D1")

    OP_D2(0x2702D6, 0x2702E0, 0xB)
    OP_D2(0x2702D7, 0x2702E1, 0xC)
    Jump("loc_8FF")

    label("loc_8E8")

    OP_D2(0x2702C2, 0x2702CC, 0xB)
    OP_D2(0x2702C3, 0x2702CD, 0xC)
    Jump("loc_8FF")

    label("loc_8FF")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_930"),
        (5, "loc_947"),
        (3, "loc_95E"),
        (4, "loc_975"),
        (6, "loc_98C"),
        (7, "loc_9A3"),
        (8, "loc_9BA"),
        (10, "loc_9D1"),
        (14, "loc_9E8"),
        (15, "loc_9FF"),
        (SWITCH_DEFAULT, "loc_A16"),
    )


    label("loc_930")

    OP_D2(0x701D0, 0x701DC, 0xD)
    OP_D2(0x701D1, 0x701DD, 0xE)
    Jump("loc_A16")

    label("loc_947")

    OP_D2(0x70218, 0x70224, 0xD)
    OP_D2(0x70219, 0x70225, 0xE)
    Jump("loc_A16")

    label("loc_95E")

    OP_D2(0x701E8, 0x701F4, 0xD)
    OP_D2(0x701E9, 0x701F5, 0xE)
    Jump("loc_A16")

    label("loc_975")

    OP_D2(0x27036E, 0x27037B, 0xD)
    OP_D2(0x27036F, 0x27037C, 0xE)
    Jump("loc_A16")

    label("loc_98C")

    OP_D2(0x70230, 0x7023C, 0xD)
    OP_D2(0x70231, 0x7023D, 0xE)
    Jump("loc_A16")

    label("loc_9A3")

    OP_D2(0x70248, 0x70254, 0xD)
    OP_D2(0x70249, 0x70255, 0xE)
    Jump("loc_A16")

    label("loc_9BA")

    OP_D2(0x270176, 0x270183, 0xD)
    OP_D2(0x270177, 0x270184, 0xE)
    Jump("loc_A16")

    label("loc_9D1")

    OP_D2(0x702B4, 0x702BB, 0xD)
    OP_D2(0x702B5, 0x702BC, 0xE)
    Jump("loc_A16")

    label("loc_9E8")

    OP_D2(0x2702D6, 0x2702E0, 0xD)
    OP_D2(0x2702D7, 0x2702E1, 0xE)
    Jump("loc_A16")

    label("loc_9FF")

    OP_D2(0x2702C2, 0x2702CC, 0xD)
    OP_D2(0x2702C3, 0x2702CD, 0xE)
    Jump("loc_A16")

    label("loc_A16")

    OP_D2(0x27028E, 0x270298, 0xF)
    OP_D2(0x27028F, 0x270299, 0x10)
    OP_D2(0x270290, 0x27029A, 0x11)
    OP_D2(0x270293, 0x27029D, 0x12)
    OP_D2(0x270296, 0x2702A0, 0x13)
    OP_D2(0x29021E, 0x290222, 0x14)
    OP_D2(0x29021F, 0x290223, 0x15)
    OP_D2(0x27034E, 0x27035E, 0x16)
    OP_D2(0x27034F, 0x27035F, 0x17)
    OP_D2(0x270350, 0x270360, 0x18)
    OP_D2(0x290226, 0x290227, 0x19)
    LoadEffect(0x0, "monster\\msc0647.eff")
    LoadEffect(0x1, "craft\\cr163_01.eff")
    Return()

    # Function_3_754 end

    def Function_4_AB0(): pass

    label("Function_4_AB0")

    OP_D2(0x270132, 0x270142, 0x0)
    OP_D2(0x270132, 0x270142, 0x1)
    OP_D2(0x27027E, 0x270288, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x270111, 0x270121, 0x4)
    OP_D2(0x270114, 0x270124, 0x5)
    OP_D2(0x27034E, 0x27035E, 0x6)
    OP_D2(0x27034F, 0x27035F, 0x7)
    OP_D2(0x270350, 0x270360, 0x8)
    OP_D2(0x270352, 0x270362, 0x9)
    OP_D2(0x270357, 0x270367, 0xA)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_B4F"),
        (5, "loc_B66"),
        (3, "loc_B7D"),
        (4, "loc_B94"),
        (6, "loc_BAB"),
        (7, "loc_BC2"),
        (8, "loc_BD9"),
        (10, "loc_BF0"),
        (14, "loc_C07"),
        (15, "loc_C1E"),
        (SWITCH_DEFAULT, "loc_C35"),
    )


    label("loc_B4F")

    OP_D2(0x701D0, 0x701DC, 0xB)
    OP_D2(0x701D1, 0x701DD, 0xC)
    Jump("loc_C35")

    label("loc_B66")

    OP_D2(0x70218, 0x70224, 0xB)
    OP_D2(0x70219, 0x70225, 0xC)
    Jump("loc_C35")

    label("loc_B7D")

    OP_D2(0x701E8, 0x701F4, 0xB)
    OP_D2(0x701E9, 0x701F5, 0xC)
    Jump("loc_C35")

    label("loc_B94")

    OP_D2(0x27036E, 0x27037B, 0xB)
    OP_D2(0x27036F, 0x27037C, 0xC)
    Jump("loc_C35")

    label("loc_BAB")

    OP_D2(0x70230, 0x7023C, 0xB)
    OP_D2(0x70231, 0x7023D, 0xC)
    Jump("loc_C35")

    label("loc_BC2")

    OP_D2(0x70248, 0x70254, 0xB)
    OP_D2(0x70249, 0x70255, 0xC)
    Jump("loc_C35")

    label("loc_BD9")

    OP_D2(0x270176, 0x270183, 0xB)
    OP_D2(0x270177, 0x270184, 0xC)
    Jump("loc_C35")

    label("loc_BF0")

    OP_D2(0x702B4, 0x702BB, 0xB)
    OP_D2(0x702B5, 0x702BC, 0xC)
    Jump("loc_C35")

    label("loc_C07")

    OP_D2(0x2702D6, 0x2702E0, 0xB)
    OP_D2(0x2702D7, 0x2702E1, 0xC)
    Jump("loc_C35")

    label("loc_C1E")

    OP_D2(0x2702C2, 0x2702CC, 0xB)
    OP_D2(0x2702C3, 0x2702CD, 0xC)
    Jump("loc_C35")

    label("loc_C35")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_C66"),
        (5, "loc_C7D"),
        (3, "loc_C94"),
        (4, "loc_CAB"),
        (6, "loc_CC2"),
        (7, "loc_CD9"),
        (8, "loc_CF0"),
        (10, "loc_D07"),
        (14, "loc_D1E"),
        (15, "loc_D35"),
        (SWITCH_DEFAULT, "loc_D4C"),
    )


    label("loc_C66")

    OP_D2(0x701D0, 0x701DC, 0xD)
    OP_D2(0x701D1, 0x701DD, 0xE)
    Jump("loc_D4C")

    label("loc_C7D")

    OP_D2(0x70218, 0x70224, 0xD)
    OP_D2(0x70219, 0x70225, 0xE)
    Jump("loc_D4C")

    label("loc_C94")

    OP_D2(0x701E8, 0x701F4, 0xD)
    OP_D2(0x701E9, 0x701F5, 0xE)
    Jump("loc_D4C")

    label("loc_CAB")

    OP_D2(0x27036E, 0x27037B, 0xD)
    OP_D2(0x27036F, 0x27037C, 0xE)
    Jump("loc_D4C")

    label("loc_CC2")

    OP_D2(0x70230, 0x7023C, 0xD)
    OP_D2(0x70231, 0x7023D, 0xE)
    Jump("loc_D4C")

    label("loc_CD9")

    OP_D2(0x70248, 0x70254, 0xD)
    OP_D2(0x70249, 0x70255, 0xE)
    Jump("loc_D4C")

    label("loc_CF0")

    OP_D2(0x270176, 0x270183, 0xD)
    OP_D2(0x270177, 0x270184, 0xE)
    Jump("loc_D4C")

    label("loc_D07")

    OP_D2(0x702B4, 0x702BB, 0xD)
    OP_D2(0x702B5, 0x702BC, 0xE)
    Jump("loc_D4C")

    label("loc_D1E")

    OP_D2(0x2702D6, 0x2702E0, 0xD)
    OP_D2(0x2702D7, 0x2702E1, 0xE)
    Jump("loc_D4C")

    label("loc_D35")

    OP_D2(0x2702C2, 0x2702CC, 0xD)
    OP_D2(0x2702C3, 0x2702CD, 0xE)
    Jump("loc_D4C")

    label("loc_D4C")

    OP_D2(0x27028E, 0x270298, 0xF)
    OP_D2(0x27028F, 0x270299, 0x10)
    OP_D2(0x270290, 0x27029A, 0x11)
    OP_D2(0x2601EE, 0x2601F3, 0x12)
    OP_D2(0x270296, 0x2702A0, 0x13)
    OP_D2(0x29021E, 0x290222, 0x14)
    OP_D2(0x70148, 0x7014C, 0x15)
    OP_D2(0x27027A, 0x270284, 0x16)
    OP_D2(0x27027C, 0x270286, 0x17)
    OP_D2(0x27027D, 0x270287, 0x18)
    Return()

    # Function_4_AB0 end

    def Function_5_DB1(): pass

    label("Function_5_DB1")

    OP_D2(0x26011B, 0x260120, 0x0)
    OP_D2(0x2601E2, 0x2601E7, 0x1)
    OP_D2(0x2601E6, 0x2601EB, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x270111, 0x270121, 0x4)
    OP_D2(0x270114, 0x270124, 0x5)
    OP_D2(0x27034E, 0x27035E, 0x6)
    OP_D2(0x27034F, 0x27035F, 0x7)
    OP_D2(0x270350, 0x270360, 0x8)
    OP_D2(0x270352, 0x270362, 0x9)
    OP_D2(0x270357, 0x270367, 0xA)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_E50"),
        (5, "loc_E67"),
        (3, "loc_E7E"),
        (4, "loc_E95"),
        (6, "loc_EAC"),
        (7, "loc_EC3"),
        (8, "loc_EDA"),
        (10, "loc_EF1"),
        (14, "loc_F08"),
        (15, "loc_F1F"),
        (SWITCH_DEFAULT, "loc_F36"),
    )


    label("loc_E50")

    OP_D2(0x701D0, 0x701DC, 0xB)
    OP_D2(0x701D1, 0x701DD, 0xC)
    Jump("loc_F36")

    label("loc_E67")

    OP_D2(0x70218, 0x70224, 0xB)
    OP_D2(0x70219, 0x70225, 0xC)
    Jump("loc_F36")

    label("loc_E7E")

    OP_D2(0x701E8, 0x701F4, 0xB)
    OP_D2(0x701E9, 0x701F5, 0xC)
    Jump("loc_F36")

    label("loc_E95")

    OP_D2(0x27036E, 0x27037B, 0xB)
    OP_D2(0x27036F, 0x27037C, 0xC)
    Jump("loc_F36")

    label("loc_EAC")

    OP_D2(0x70230, 0x7023C, 0xB)
    OP_D2(0x70231, 0x7023D, 0xC)
    Jump("loc_F36")

    label("loc_EC3")

    OP_D2(0x70248, 0x70254, 0xB)
    OP_D2(0x70249, 0x70255, 0xC)
    Jump("loc_F36")

    label("loc_EDA")

    OP_D2(0x270176, 0x270183, 0xB)
    OP_D2(0x270177, 0x270184, 0xC)
    Jump("loc_F36")

    label("loc_EF1")

    OP_D2(0x702B4, 0x702BB, 0xB)
    OP_D2(0x702B5, 0x702BC, 0xC)
    Jump("loc_F36")

    label("loc_F08")

    OP_D2(0x2702D6, 0x2702E0, 0xB)
    OP_D2(0x2702D7, 0x2702E1, 0xC)
    Jump("loc_F36")

    label("loc_F1F")

    OP_D2(0x2702C2, 0x2702CC, 0xB)
    OP_D2(0x2702C3, 0x2702CD, 0xC)
    Jump("loc_F36")

    label("loc_F36")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_F67"),
        (5, "loc_F7E"),
        (3, "loc_F95"),
        (4, "loc_FAC"),
        (6, "loc_FC3"),
        (7, "loc_FDA"),
        (8, "loc_FF1"),
        (10, "loc_1008"),
        (14, "loc_101F"),
        (15, "loc_1036"),
        (SWITCH_DEFAULT, "loc_104D"),
    )


    label("loc_F67")

    OP_D2(0x701D0, 0x701DC, 0xD)
    OP_D2(0x701D1, 0x701DD, 0xE)
    Jump("loc_104D")

    label("loc_F7E")

    OP_D2(0x70218, 0x70224, 0xD)
    OP_D2(0x70219, 0x70225, 0xE)
    Jump("loc_104D")

    label("loc_F95")

    OP_D2(0x701E8, 0x701F4, 0xD)
    OP_D2(0x701E9, 0x701F5, 0xE)
    Jump("loc_104D")

    label("loc_FAC")

    OP_D2(0x27036E, 0x27037B, 0xD)
    OP_D2(0x27036F, 0x27037C, 0xE)
    Jump("loc_104D")

    label("loc_FC3")

    OP_D2(0x70230, 0x7023C, 0xD)
    OP_D2(0x70231, 0x7023D, 0xE)
    Jump("loc_104D")

    label("loc_FDA")

    OP_D2(0x70248, 0x70254, 0xD)
    OP_D2(0x70249, 0x70255, 0xE)
    Jump("loc_104D")

    label("loc_FF1")

    OP_D2(0x270176, 0x270183, 0xD)
    OP_D2(0x270177, 0x270184, 0xE)
    Jump("loc_104D")

    label("loc_1008")

    OP_D2(0x702B4, 0x702BB, 0xD)
    OP_D2(0x702B5, 0x702BC, 0xE)
    Jump("loc_104D")

    label("loc_101F")

    OP_D2(0x2702D6, 0x2702E0, 0xD)
    OP_D2(0x2702D7, 0x2702E1, 0xE)
    Jump("loc_104D")

    label("loc_1036")

    OP_D2(0x2702C2, 0x2702CC, 0xD)
    OP_D2(0x2702C3, 0x2702CD, 0xE)
    Jump("loc_104D")

    label("loc_104D")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_107E"),
        (5, "loc_108B"),
        (3, "loc_1098"),
        (4, "loc_10A5"),
        (6, "loc_10B2"),
        (7, "loc_10BF"),
        (8, "loc_10CC"),
        (10, "loc_10D9"),
        (14, "loc_10E6"),
        (15, "loc_10F3"),
        (SWITCH_DEFAULT, "loc_1100"),
    )


    label("loc_107E")

    OP_D2(0x701D4, 0x701E0, 0xF)
    Jump("loc_1100")

    label("loc_108B")

    OP_D2(0x7021C, 0x70228, 0xF)
    Jump("loc_1100")

    label("loc_1098")

    OP_D2(0x701EC, 0x701F8, 0xF)
    Jump("loc_1100")

    label("loc_10A5")

    OP_D2(0x270372, 0x27037F, 0xF)
    Jump("loc_1100")

    label("loc_10B2")

    OP_D2(0x70234, 0x70240, 0xF)
    Jump("loc_1100")

    label("loc_10BF")

    OP_D2(0x7024C, 0x70258, 0xF)
    Jump("loc_1100")

    label("loc_10CC")

    OP_D2(0x27017A, 0x270187, 0xF)
    Jump("loc_1100")

    label("loc_10D9")

    OP_D2(0x702B8, 0x702BF, 0xF)
    Jump("loc_1100")

    label("loc_10E6")

    OP_D2(0x2702DA, 0x2702E4, 0xF)
    Jump("loc_1100")

    label("loc_10F3")

    OP_D2(0x2702C6, 0x2702D0, 0xF)
    Jump("loc_1100")

    label("loc_1100")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1131"),
        (5, "loc_113E"),
        (3, "loc_114B"),
        (4, "loc_1158"),
        (6, "loc_1165"),
        (7, "loc_1172"),
        (8, "loc_117F"),
        (10, "loc_118C"),
        (14, "loc_1199"),
        (15, "loc_11A6"),
        (SWITCH_DEFAULT, "loc_11B3"),
    )


    label("loc_1131")

    OP_D2(0x701D4, 0x701E0, 0x10)
    Jump("loc_11B3")

    label("loc_113E")

    OP_D2(0x7021C, 0x70228, 0x10)
    Jump("loc_11B3")

    label("loc_114B")

    OP_D2(0x701EC, 0x701F8, 0x10)
    Jump("loc_11B3")

    label("loc_1158")

    OP_D2(0x270372, 0x27037F, 0x10)
    Jump("loc_11B3")

    label("loc_1165")

    OP_D2(0x70234, 0x70240, 0x10)
    Jump("loc_11B3")

    label("loc_1172")

    OP_D2(0x7024C, 0x70258, 0x10)
    Jump("loc_11B3")

    label("loc_117F")

    OP_D2(0x27017A, 0x270187, 0x10)
    Jump("loc_11B3")

    label("loc_118C")

    OP_D2(0x702B8, 0x702BF, 0x10)
    Jump("loc_11B3")

    label("loc_1199")

    OP_D2(0x2702DA, 0x2702E4, 0x10)
    Jump("loc_11B3")

    label("loc_11A6")

    OP_D2(0x2702C6, 0x2702D0, 0x10)
    Jump("loc_11B3")

    label("loc_11B3")

    OP_D2(0x260228, 0x26022A, 0x11)
    OP_D2(0x27027E, 0x270288, 0x12)
    OP_D2(0x270280, 0x27028A, 0x13)
    OP_D2(0x260143, 0x260148, 0x14)
    OP_D2(0x70148, 0x7014C, 0x15)
    OP_D2(0x27027A, 0x270284, 0x16)
    OP_D2(0x27027C, 0x270286, 0x17)
    OP_D2(0x27027D, 0x270287, 0x18)
    Return()

    # Function_5_DB1 end

    def Function_6_1204(): pass

    label("Function_6_1204")

    Call(0, 7)
    Call(0, 8)
    Call(0, 9)
    Call(0, 10)
    Call(0, 11)
    Return()

    # Function_6_1204 end

    def Function_7_1219(): pass

    label("Function_7_1219")

    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    ClearMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_123D")
    Call(0, 33)
    Call(0, 34)
    RemoveParty(0x1, 0xFF)

    label("loc_123D")

    AddParty(0x1, 0xF7, 0xFF)
    Call(0, 2)
    OP_6D(-46590, 100, 300, 0)
    OP_67(0, 8250, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(45000, 0)
    OP_6E(369, 0)
    OP_E5(0x8, 0x0, 0x0)
    SetChrChipByIndex(0x8, 15)
    SetChrPos(0x8, -1440, 3200, 70, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x102, -2100, 3200, -950, 270)
    SetChrChipByIndex(0x102, 22)
    SetChrPos(0x101, -48040, 100, -320, 90)
    SetChrPos(0xF9, -49300, 100, 560, 90)
    SetChrPos(0xF8, -49640, 100, -940, 90)

    def lambda_12F0():
        OP_8E(0xFE, 0xFFFF5010, 0x64, 0xFFFFFEC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12F0)

    def lambda_130B():
        OP_8E(0xFE, 0xFFFF4B24, 0x64, 0x230, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_130B)

    def lambda_1326():
        OP_8E(0xFE, 0xFFFF49D0, 0x64, 0xFFFFFC54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1326)
    FadeToBright(1000, 0)
    OP_6D(-44950, 100, -470, 2000)
    WaitChrThread(0x101, 0x1)
    OP_20(0x3E8)

    ChrTalk(    #0
        0x8,
        (
            "Welcome, everyone.\x01",
            "Welcome to the home of all that is sacred.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E5")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1423")

    label("loc_13E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140C")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1423")

    label("loc_140C")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1423")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_148D")

    label("loc_144F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1476")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_148D")

    label("loc_1476")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_148D")

    Sleep(500)
    OP_21()
    OP_1D(0x70)
    Sleep(500)
    Sleep(100)
    Fade(1000)
    OP_E8(0xD0, 0x7, 0x0, 0x0)
    OP_6D(-27410, 100, -350, 0)
    OP_67(0, 3070, -10000, 0)
    OP_6B(6840, 0)
    OP_6C(78000, 0)
    OP_6E(500, 0)

    def lambda_14EC():
        OP_6D(3190, 2700, 60, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14EC)

    def lambda_1504():
        OP_67(0, 2140, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1504)

    def lambda_151C():
        OP_6B(5000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_151C)

    def lambda_152C():
        OP_6C(90000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_152C)
    Sleep(1000)

    def lambda_1541():
        OP_8E(0xFE, 0xFFFFBD98, 0xC8, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1541)
    Sleep(100)

    def lambda_1561():
        OP_8E(0xFE, 0xFFFFB726, 0xC8, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1561)
    Sleep(50)

    def lambda_1581():
        OP_8E(0xFE, 0xFFFFB7BC, 0xC8, 0xFFFFFC18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1581)
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(900, 2760, 250, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(91000, 0)
    OP_6E(524, 0)
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_0D()
    SetChrPos(0x101, -10000, 200, 0, 90)
    SetChrPos(0xF9, -11650, 200, 1000, 90)
    SetChrPos(0xF8, -11500, 200, -1000, 90)
    OP_E5(0x8, 0x0, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0x101,
        "#1020F#5PJoshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1058F#6P.    .    .\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#1151F#6PYou passed the final trial!\x01",
            "Excellent, excellent.\x02\x03",

            "Be proud! You are worthy to be present\x01",
            "for the resurrection of the Shining Ring...\x01",
            "the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1022F#5PYeah, not interested in that at all,\x01",
            "thanks!\x02\x03",

            "I'm here to put a stop to all this stupid\x01",
            "weirdness!\x02\x03",

            "#1005FAnd...I'm here to get Joshua back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#1154F#6PAh, yes. Sadly, I'm afraid that\x01",
            "won't be happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1020F#5P#3SWhat do you mean?!\x01",
            "Joshua! Hey!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#1150F#6PNo matter how you try to deny it, the\x01",
            "truth remains--Joshua's mind is little\x01",
            "more than a construct.\x02\x03",

            "The Stigma on his shoulder is proof.\x02\x03",

            "#1151FProof that he is of Ouroboros.\x01",
            "That he is my possession.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1005F#5PHow dare you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#1151F#6PPerhaps if Joshua had somehow erased\x01",
            "the Stigma of his own will, he could have\x01",
            "found release.\x02\x03",

            "But, alas, he never managed to get that far.\x02\x03",

            "It would be best if I kept him as a research\x01",
            "subject for a bit longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1002F#5P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A07")

    ChrTalk(    #11
        0x10B,
        "#216FYou...\x02",
    )

    CloseMessageWindow()

    label("loc_1A07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3A")

    ChrTalk(    #12
        0x105,
        "#1162FSuch unbelievable evil...\x02",
    )

    CloseMessageWindow()

    label("loc_1A3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A62")

    ChrTalk(    #13
        0x103,
        "#523FYou monster!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B13")

    label("loc_1A62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A88")

    ChrTalk(    #14
        0x108,
        "#077FYou beast!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B13")

    label("loc_1A88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AD5")

    ChrTalk(    #15
        0x109,
        (
            "#1063FYou really are as much of a\x01",
            "monster as they say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B13")

    label("loc_1AD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B13")

    ChrTalk(    #16
        0x10F,
        (
            "#175FYou truly are a mad beast,\x01",
            "Weissmann.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B71")

    ChrTalk(    #17
        0x106,
        (
            "#057FKeep talkin', pal. It'll make beatin'\x01",
            "your face in that much sweeter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA5")

    ChrTalk(    #18
        0x110,
        "#272FEnough of your foolishness.\x02",
    )

    CloseMessageWindow()

    label("loc_1BA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BCB")

    ChrTalk(    #19
        0x107,
        "#065FThat's awful!\x02",
    )

    CloseMessageWindow()

    label("loc_1BCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C18")

    ChrTalk(    #20
        0x104,
        (
            "#034FYou are so revolting, it almost\x01",
            "moves man to poetry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C18")


    ChrTalk(    #21
        0x8,
        (
            "#1154F#6PGoodness me! Such insults.\x01",
            "And how impotent they are.\x02\x03",

            "#1150FYou see, I suspect Joshua realized\x01",
            "very quickly what the Stigma on his\x01",
            "shoulder meant.\x02\x03",

            "Surely, he knew something like this\x01",
            "exact situation would occur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1020F#5P#3SAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#1154F#6PYet he never breathed a word of\x01",
            "his troubles to any of you, did he?\x01",
            "Not even a whisper.\x02\x03",

            "And conversely, none of you were\x01",
            "sensitive enough to notice his pain.\x02\x03",

            "#1151FWhat power these 'bonds' of yours\x01",
            "have! What complete, earth-shaking\x01",
            "potential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1003F#5PI...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E47")

    ChrTalk(    #25
        0x105,
        "#1169FAh...\x02",
    )

    CloseMessageWindow()

    label("loc_1E47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E68")

    ChrTalk(    #26
        0x10B,
        "#215FMmph...!\x02",
    )

    CloseMessageWindow()

    label("loc_1E68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E87")

    ChrTalk(    #27
        0x107,
        "#561FAww...\x02",
    )

    CloseMessageWindow()

    label("loc_1E87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB0")

    ChrTalk(    #28
        0x103,
        "#523FHow dare you...!\x02",
    )

    CloseMessageWindow()

    label("loc_1EB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ECF")

    ChrTalk(    #29
        0x10F,
        "#176FYou...\x02",
    )

    CloseMessageWindow()

    label("loc_1ECF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EEB")

    ChrTalk(    #30
        0x108,
        "#072F...\x02",
    )

    CloseMessageWindow()

    label("loc_1EEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0A")

    ChrTalk(    #31
        0x106,
        "#552FTch...\x02",
    )

    CloseMessageWindow()

    label("loc_1F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F26")

    ChrTalk(    #32
        0x104,
        "#032F...\x02",
    )

    CloseMessageWindow()

    label("loc_1F26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F42")

    ChrTalk(    #33
        0x110,
        "#276F...\x02",
    )

    CloseMessageWindow()

    label("loc_1F42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F5F")

    ChrTalk(    #34
        0x109,
        "#1063F...\x02",
    )

    CloseMessageWindow()

    label("loc_1F5F")


    ChrTalk(    #35
        0x8,
        (
            "#1154F#6PBut come now, there's no need\x01",
            "for long faces.\x02\x03",

            "#1150FYou have been granted the privilege\x01",
            "of being here for this glorious moment!\x02\x03",

            "All that remains now is to make the\x01",
            "correct choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1026F#5PPrivilege? Choice?\x02\x03",

            "What ARE you going on about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#1150F#6PPerhaps I should start from the very\x01",
            "beginning. How much DO you know,\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20C6():
        OP_6D(5920, 8840, 70, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20C6)

    def lambda_20DE():
        OP_67(0, 3770, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20DE)
    OP_6B(2850, 3000)
    Sleep(500)

    ChrTalk(    #38
        0x8,
        (
            "#1151F#5PAbout this city, and the events that\x01",
            "occurred here with the Aureole nearly\x01",
            "twelve hundred years before our time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1020F#5PUmm...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21CA")

    ChrTalk(    #40
        0x109,
        "#1063F#5PSo that's the Aureole...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2387")

    label("loc_21CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2202")

    ChrTalk(    #41
        0x105,
        "#1162F#5PSo that's the Aureole...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2387")

    label("loc_2202")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_223E")

    ChrTalk(    #42
        0x104,
        "#032F#5PSo that truly is the Aureole.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2387")

    label("loc_223E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2271")

    ChrTalk(    #43
        0x10F,
        "#178FSo that is the Aureole.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2387")

    label("loc_2271")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22A6")

    ChrTalk(    #44
        0x103,
        "#022F#5PSo that's the Aureole.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2387")

    label("loc_22A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22DB")

    ChrTalk(    #45
        0x108,
        "#072F#5PSo that's the Aureole.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2387")

    label("loc_22DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_231D")

    ChrTalk(    #46
        0x106,
        "#057F#5PSo that thing there is the Aureole.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2387")

    label("loc_231D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2357")

    ChrTalk(    #47
        0x107,
        "#065F#5PAh! So that's the Aureole?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2387")

    label("loc_2357")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2387")

    ChrTalk(    #48
        0x110,
        "#270FSo that is the Aureole.\x02",
    )

    CloseMessageWindow()

    label("loc_2387")


    ChrTalk(    #49
        0x8,
        (
            "#1154F#5PIt most certainly is.\x02\x03",

            "#1152FOne of the ultimate artifacts, capable\x01",
            "of producing literally endless power and\x01",
            "shaping miracles with it!\x02\x03",

            "But the ancients sealed it away, despite\x01",
            "its limitless, science-shattering potential!\x02\x03",

            "Why do you think they would do such a\x01",
            "thing?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2649")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as viewed all deciphered terminal data\x01",                                      # 0
            "Set as viewed half or more of deciphered terminal data\x01",                          # 1
            "Set as did not read more than a minimal amount of deciphered terminal data\x01",      # 2
            "No change\x01",                                                                       # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25A2"),
        (1, "loc_25D5"),
        (2, "loc_2608"),
        (SWITCH_DEFAULT, "loc_263B"),
    )


    label("loc_25A2")

    OP_A2(0x2280)
    OP_A2(0x2281)
    OP_A2(0x2282)
    OP_A2(0x2283)
    OP_A2(0x2284)
    OP_A2(0x2285)
    OP_A2(0x2286)
    OP_A2(0x2287)
    OP_A2(0x2288)
    OP_A2(0x2289)
    OP_A2(0x228A)
    OP_A2(0x228B)
    OP_A2(0x2276)
    OP_A2(0x2277)
    OP_A2(0x2278)
    OP_A2(0x2279)
    Jump("loc_263B")

    label("loc_25D5")

    OP_A2(0x2280)
    OP_A2(0x2281)
    OP_A2(0x2282)
    OP_A2(0x2283)
    OP_A2(0x2284)
    OP_A2(0x2285)
    OP_A2(0x2286)
    OP_A2(0x2287)
    OP_A3(0x2288)
    OP_A3(0x2289)
    OP_A3(0x228A)
    OP_A3(0x228B)
    OP_A3(0x2276)
    OP_A3(0x2277)
    OP_A3(0x2278)
    OP_A3(0x2279)
    Jump("loc_263B")

    label("loc_2608")

    OP_A3(0x2280)
    OP_A3(0x2281)
    OP_A3(0x2282)
    OP_A3(0x2283)
    OP_A3(0x2284)
    OP_A3(0x2285)
    OP_A3(0x2286)
    OP_A3(0x2287)
    OP_A3(0x2288)
    OP_A3(0x2289)
    OP_A3(0x228A)
    OP_A3(0x228B)
    OP_A3(0x2276)
    OP_A3(0x2277)
    OP_A3(0x2278)
    OP_A3(0x2279)
    Jump("loc_263B")

    label("loc_263B")

    FadeToBright(300, 0)
    Sleep(500)

    label("loc_2649")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 0)), scpexpr(EXPR_END)), "loc_2664")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 1)), scpexpr(EXPR_END)), "loc_2675")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 2)), scpexpr(EXPR_END)), "loc_2686")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 3)), scpexpr(EXPR_END)), "loc_2697")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 4)), scpexpr(EXPR_END)), "loc_26A8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_26A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 5)), scpexpr(EXPR_END)), "loc_26B9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_26B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 6)), scpexpr(EXPR_END)), "loc_26CA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_26CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 7)), scpexpr(EXPR_END)), "loc_26DB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_26DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 0)), scpexpr(EXPR_END)), "loc_26EC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_26EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 1)), scpexpr(EXPR_END)), "loc_26FD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_26FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 2)), scpexpr(EXPR_END)), "loc_270E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_270E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 3)), scpexpr(EXPR_END)), "loc_271F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_271F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44E, 6)), scpexpr(EXPR_END)), "loc_2730")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44E, 7)), scpexpr(EXPR_END)), "loc_2741")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44F, 0)), scpexpr(EXPR_END)), "loc_2752")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44F, 1)), scpexpr(EXPR_END)), "loc_2763")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2763")

    Sleep(100)
    Fade(500)
    OP_6D(-16640, 200, 780, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(45000, 0)
    OP_6E(415, 0)
    SetChrPos(0x101, -17120, 200, -110, 90)
    SetChrPos(0xF9, -18040, 200, 590, 90)
    SetChrPos(0xF8, -18430, 200, -1130, 90)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_295A")

    ChrTalk(    #50
        0x101,
        (
            "#1003F#6PI don't know the whole story,\x01",
            "I'm sure, but...\x02\x03",

            "#1002FThe data left in the towers said\x01",
            "it was having a bad influence on\x01",
            "people and society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#1153F#6PAhhh. You actually managed to put all\x01",
            "those together, did you?\x02\x03",

            "#1150FThat will make this quick, then. Allow me\x01",
            "to play the role of professor once more and\x01",
            "elucidate the truth of the matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4F")

    label("loc_295A")


    ChrTalk(    #52
        0x101,
        "#1003F#6PUm, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#1154F#6PAh, you were too busy struggling\x01",
            "with what was before you to bother\x01",
            "learning anything, I suppose.\x02\x03",

            "#1150FWell, then. Allow me to play the role\x01",
            "of professor once more and elucidate\x01",
            "the truth of the matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4F")

    Sleep(200)
    Fade(1000)
    OP_E8(0xD0, 0x7, 0x0, 0x0)
    OP_6D(0, 3120, 1690, 0)
    OP_67(0, 3940, -10000, 0)
    OP_6B(1960, 0)
    OP_6C(45000, 0)
    OP_6E(524, 0)

    def lambda_2AA1():
        OP_6D(1490, 2940, 3620, 20000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AA1)

    def lambda_2AB9():
        OP_67(0, 8210, -10000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AB9)

    def lambda_2AD1():
        OP_6B(2780, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AD1)

    def lambda_2AE1():
        OP_6C(303000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2AE1)

    def lambda_2AF1():
        OP_6E(583, 20000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AF1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetMessageWindowPos(-1, 320, 40, 3)
    SetChrName("Weissmann")

    AnonymousTalk(    #54
        (
            "\x07\x00#1154FMillennia ago, Aidios of the Sky granted humanity\x01",
            "the Seven Treasures.\x02\x03",

            "For brevity's sake, we'll say each one utilized a\x01",
            "'facet of reality' in order to manifest miracles in\x01",
            "their own way.\x02\x03",

            "#1150FHumanity split into seven factions, each centered\x01",
            "around a treasure, to pursue an ideal based on\x01",
            "the powers of the given treasure.\x02\x03",

            "One such ideal was this--Liber Ark, a city in the\x01",
            "sky with the Aureole at its center.\x02\x03",

            "#1154FA paradise, removed from the troubles of the\x01",
            "ground, where each man's 'Gospel' could grant\x01",
            "any wish through the Aureole...\x02\x03",

            "Mankind lived a bountiful life here,\x01",
            "absolutely free of strife.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #55
        (
            "\x07\x00#1152FOver time, however, people's lives were swallowed\x01",
            "up in the artificial bliss granted to them by the\x01",
            "Aureole.\x02\x03",

            "Not just physical ecstasy, but even dreams\x01",
            "were provided by the Aureole--false realities\x01",
            "granted people long-sought spiritual fulfillment.\x02\x03",

            "The people of Liber Ark, dependent on 'miracles'\x01",
            "that were all but a narcotic, began treading the\x01",
            "path to annihilation.\x02\x03",

            "#1154FThe Ark's inhabitants lost all sense of ambition\x01",
            "and ethics, and slid into madness and despair.\x02\x03",

            "Birth rates dropped catastrophically while suicide\x01",
            "and bizarre crime ran rampant, and the whole of\x01",
            "society walked the path to a slow demise.\x02\x03",

            "#1152FBut the Aureole passed no judgment on these\x01",
            "people. It merely granted the miracles asked\x01",
            "of it.\x02\x03",

            "And so the shining jewel of the sky became a den\x01",
            "of evil and chaos.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x1)
    Sleep(100)
    Fade(500)
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_6D(900, 2760, 250, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(91000, 0)
    OP_6E(524, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -10000, 200, 0, 90)
    SetChrPos(0xF9, -11650, 200, 1000, 90)
    SetChrPos(0xF8, -11500, 200, -1000, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x8,
        (
            "#1150F#6PThis was the situation Celeste Auslese and her\x01",
            "conspirators faced over one thousand years ago.\x02\x03",

            "They built the seal and the device towers\x01",
            "even as they fought off the guardians of the\x01",
            "Aureole, which it sent forth to 'save' itself...\x02\x03",

            "#1154FAnd, at last, they sealed not just the Aureole,\x01",
            "but the entire city, in another dimension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1020F#5PThat's what happened twelve\x01",
            "hundred years ago...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3327")

    ChrTalk(    #58
        0x105,
        "#1163FI never would have imagined...\x02",
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_3327")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_336F")

    ChrTalk(    #59
        0x104,
        (
            "#032FIt does ultimately fit with what\x01",
            "we've seen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_336F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_339E")

    ChrTalk(    #60
        0x10F,
        "#175FI never imagined...\x02",
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_339E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33CD")

    ChrTalk(    #61
        0x107,
        "#065FIt got that bad...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_33CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33FE")

    ChrTalk(    #62
        0x108,
        "#074FThings were that bad...?\x02",
    )

    CloseMessageWindow()

    label("loc_33FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3431")

    ChrTalk(    #63
        0x106,
        "#552FDamn, that's messed up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_34EE")

    label("loc_3431")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3469")

    ChrTalk(    #64
        0x103,
        "#522FHard to even believe that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_34EE")

    label("loc_3469")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34AA")

    ChrTalk(    #65
        0x10B,
        "#413FI dunno if I can even believe that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_34EE")

    label("loc_34AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34EE")

    ChrTalk(    #66
        0x110,
        "#272F...Much what I'd expect of ancient history.\x02",
    )

    CloseMessageWindow()

    label("loc_34EE")


    ChrTalk(    #67
        0x8,
        (
            "#1154F#6PI will grant that the elder Ausleses did\x01",
            "quite well, given the circumstances.\x02\x03",

            "#1152FBut...think for a moment.\x02\x03",

            "The cost of Celeste's 'victory' was\x01",
            "humanity being cast forth into a land of chaos,\x01",
            "forced to start again from nearly nothing.\x02\x03",

            "Think of all the suffering man endured then,\x01",
            "and endures now, as man savages one another\x01",
            "with endless, petty wars.\x02\x03",

            "Can it truly be said that she made the right\x01",
            "decision?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1026F#5PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#1152F#6POn the other hand, we have gained\x01",
            "--or regained--orbal technology and once\x01",
            "again live bountiful, easy lives.\x02\x03",

            "At this rate, only two ends are possible.\x02\x03",

            "#1154FEither we continuously seek to dominate one\x01",
            "another and, unable to control ourselves,\x01",
            "obliterate each other in an orgy of conflict...\x02\x03",

            "Or, like the people of old, we sink into narcotic\x01",
            "self-pleasure, let automated systems run the\x01",
            "world, and live as farm animals.\x02\x03",

            "#1151FEither physical or mental annihilation awaits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1026F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "#1152F#6PThere is but one single path for humanity if it\x01",
            "wishes to survive.\x02\x03",

            "#1154FThe beasts of mankind must be led to the\x01",
            "point where they obtain the two things required\x01",
            "for TRUE, enlightened sentience...\x02\x03",

            "A flawless rationality, capable of resisting any\x01",
            "temptation and unswayed by even the fiercest\x01",
            "circumstances!\x02\x03",

            "And peerless intelligence, ever capable of\x01",
            "finding the correct solution, unmoved by crude\x01",
            "emotion!\x02\x03",

            "#1151FThis is the true goal of the Gospel Plan!\x01",
            "To do what even the ancients could not!\x01",
            "To advance our minds to what they SHOULD be!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B09")

    ChrTalk(    #72
        0x109,
        "#1063FYou're...actually serious.\x02",
    )

    CloseMessageWindow()

    label("loc_3B09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B2D")

    ChrTalk(    #73
        0x10F,
        "#178FMadness!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B50")

    label("loc_3B2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B50")

    ChrTalk(    #74
        0x107,
        "#065FI don't...\x02",
    )

    CloseMessageWindow()

    label("loc_3B50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B7B")

    ChrTalk(    #75
        0x108,
        "#572FWhat madness...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BE3")

    label("loc_3B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BBA")

    ChrTalk(    #76
        0x104,
        "#034FAn ambitious goal, if nothing else.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BE3")

    label("loc_3BBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BE3")

    ChrTalk(    #77
        0x105,
        "#1169FWhat madness...\x02",
    )

    CloseMessageWindow()

    label("loc_3BE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C19")

    ChrTalk(    #78
        0x110,
        "#276FHmph. Good luck with that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3C19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C55")

    ChrTalk(    #79
        0x106,
        "#552FYou're screwed in the head, pal.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3C55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C8B")

    ChrTalk(    #80
        0x103,
        "#522FMad words from a madman...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3C8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CCA")

    ChrTalk(    #81
        0x10B,
        "#215FBoy, now I know what crazy looks like.\x02",
    )

    CloseMessageWindow()

    label("loc_3CCA")


    ChrTalk(    #82
        0x8,
        (
            "#1151F#6PI would so appreciate it if you would not look\x01",
            "at me as if I were a megalomaniacal lunatic.\x02\x03",

            "#1150FMan cannot help but change and reform\x01",
            "through fear when confronted with something\x01",
            "beyond his imagining.\x02\x03",

            "In that sense, what better tool exists to\x01",
            "drive evolution forward than the Aureole?\x02\x03",

            "#1154FI will guide mankind onto the correct path to\x01",
            "salvation with this great treasure from Aidios.\x02\x03",

            "#1155FTHAT is my duty as one of the Anguis!\x01",
            "My duty to Ouroboros and its master!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1007F#5P*sigh*\x02\x03",

            "#1019FBoy, I bet you're a real hit at parties.\x01",
            "Not.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #84
        0x8,
        "#1153F#6POh? What's this?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x81, 0x0)
    OP_82(0x80, 0x0)
    Fade(500)
    OP_6D(-19160, 200, 530, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(296000, 0)
    OP_6E(415, 0)
    OP_6E(415, 0)
    SetChrPos(0x101, -17120, 200, -110, 90)
    SetChrPos(0xF9, -18810, 200, 970, 90)
    SetChrPos(0xF8, -18420, 200, -1010, 90)
    SetChrPos(0x8, -7470, 200, 90, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #85
        0x101,
        (
            "#1002F#5P'A flawless rationality, capable of resisting\x01",
            "any temptation and unswayed by even the\x01",
            "fiercest circumstances'?\x02\x03",

            "'Peerless intelligence, ever capable of\x01",
            "finding the correct solution, unmoved by\x01",
            "crude emotion'?\x02\x03",

            "What's the point of any of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#1152F#5PIt seems someone was sleeping during\x01",
            "the lecture.\x02\x03",

            "As I said, mankind faces annihilation\x01",
            "through either conflict or mental entropy.\x01",
            "The only way we can--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1007F#5PNo, no. I heard the lecture just fine.\x01",
            "That's not what I'm talking about.\x02\x03",

            "#1006FWhat I'm trying to say is, isn't there\x01",
            "something we can DO about the problems\x01",
            "you described if we know they exist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        "#1152F#5PHm...?\x02",
    )

    CloseMessageWindow()

    def lambda_426A():
        OP_6B(2300, 20000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_426A)

    ChrTalk(    #89
        0x101,
        (
            "#1025F#5PIt's like Joshua said to Loewe: We aren't\x01",
            "completely powerless.\x02\x03",

            "They might not be guided by flawless, peerless\x01",
            "whatever, but everyone's working together to get\x01",
            "through the crisis going on right now.\x02\x03",

            "#1012FI've gone across all of Liberl and seen it with\x01",
            "my own eyes.\x02\x03",

            "#1006FDon't you think we're capable of getting along\x01",
            "just fine without some kind of forceful grand\x01",
            "transformation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#1151F#5PReally now. Eking out survival by flocking\x01",
            "together is how beasts and insects live.\x02\x03",

            "Is that really all you have to offer on the\x01",
            "potential of humanity as it stands now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1007F#5PIs there anything else I NEED to offer?\x01",
            "Is there a problem with being the same?\x02\x03",

            "#1006FI mean, we're living beings too, you know.\x02\x03",

            "And, heck, aren't I just talking about\x01",
            "the strength of life?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        "#1153F#5PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1006F#5PI don't think people are JUST animals,\x01",
            "of course.\x02\x03",

            "I just think that living honestly, with that\x01",
            "spark of life from others as your driving force...\x01",
            "That's what it means to live.\x02\x03",

            "#1012FPeople don't need to be omnipotent\x01",
            "superbeings or whatever you want them\x01",
            "to be.\x02\x03",

            "People just need to be aware of one\x01",
            "another and help each other out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "#1152F#5PHmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1015F#5PAnd you know what? I bet the people who\x01",
            "sealed the Aureole away in the first place felt\x01",
            "the same way.\x02\x03",

            "I mean, sure, making miracles mundane\x01",
            "and relying on nothing but them is really bad\x01",
            "by itself.\x02\x03",

            "#1007FBut the biggest problem there, more than\x01",
            "anything, is that it makes it so there's no point\x01",
            "in knowing or helping each other. That's...awful.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_487E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_487E)
    Sleep(50)

    def lambda_4891():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4891)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48D7")

    ChrTalk(    #96
        0x103,
        "#027FWell said, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A18")

    label("loc_48D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48FF")

    ChrTalk(    #97
        0x107,
        "#560FThat's true!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A18")

    label("loc_48FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_492C")

    ChrTalk(    #98
        0x105,
        "#1168F...You're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A18")

    label("loc_492C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_495A")

    ChrTalk(    #99
        0x106,
        "#051FHeh... Damn right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A18")

    label("loc_495A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4980")

    ChrTalk(    #100
        0x108,
        "#070FWell said!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A18")

    label("loc_4980")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49A4")

    ChrTalk(    #101
        0x104,
        "#030FPerfect.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A18")

    label("loc_49A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49D3")

    ChrTalk(    #102
        0x10F,
        "#171FWell said, Estelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A18")

    label("loc_49D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F8")

    ChrTalk(    #103
        0x109,
        "#1060FNot bad!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A18")

    label("loc_49F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A18")

    ChrTalk(    #104
        0x10B,
        "#213FWhoa...\x02",
    )

    CloseMessageWindow()

    label("loc_4A18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AAD")

    ChrTalk(    #105
        0x110,
        (
            "#277FAll men think they are an island, but,\x01",
            "in truth, they are made men by all the\x01",
            "others in their lives.\x02\x03",

            "#278FHeh... Indeed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4AAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B4F")

    ChrTalk(    #106
        0x10B,
        (
            "#211FHaha! Pretty sharp for an airhead.\x02\x03",

            "#210FNo man's an island, and godlike\x01",
            "intelligence won't change that. You're\x01",
            "cooler than I thought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4B4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BC8")

    ChrTalk(    #107
        0x109,
        (
            "#1065FA man can only be a man because\x01",
            "it's others who make the man.\x02\x03",

            "#1060FYou nailed it, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4BC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C82")

    ChrTalk(    #108
        0x10F,
        (
            "#179FI wholeheartedly agree.\x02\x03",

            "People survive thanks to the help\x01",
            "they give one another.\x02\x03",

            "#170FHad we lost the will to do such,\x01",
            "we would never have made it this\x01",
            "far.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4C82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D61")

    ChrTalk(    #109
        0x104,
        (
            "#035FRight before the final act comes to a close,\x01",
            "our heroine delivers a marvelous rebuttal.\x02\x03",

            "#030F'Man cannot live without other men, even\x01",
            "if he be as a god.' You speak true words\x01",
            "of wisdom, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4D61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DC6")

    ChrTalk(    #110
        0x108,
        (
            "#074FA man can only be a man\x01",
            "because he IS a man...\x02\x03",

            "#070FWise words, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4DC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E74")

    ChrTalk(    #111
        0x106,
        (
            "#053FYeah, people like to think they're islands,\x01",
            "but there's no way you can live without the\x01",
            "help of everyone else around you.\x02\x03",

            "#051FRight on, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4E74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EF4")

    ChrTalk(    #112
        0x105,
        (
            "#1167FI couldn't agree more, Estelle.\x02\x03",

            "#1168FPeople can accomplish anything,\x01",
            "so long as they're together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4EF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FB0")

    ChrTalk(    #113
        0x107,
        (
            "#560FI think so, too, Estelle!\x02\x03",

            "#563FNobody can really live totally alone.\x02\x03",

            "Everyone's connected to someone else\x01",
            "somehow, even if it's just memories, or\x01",
            "emotions, or...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB0")


    ChrTalk(    #114
        0x8,
        (
            "#1154F#5PHah... STILL sticking to the 'mutual\x01",
            "assistance' argument and invoking the\x01",
            "power of 'human bonds,' of all things...\x02\x03",

            "#1151FI would ask you to read a history book\x01",
            "before saying such nonsense, Ms. Bright.\x02\x03",

            "As an example, consider the overpowering,\x01",
            "nation-crushing machine called 'war.'\x02\x03",

            "Is man not only capable of being ground\x01",
            "beneath its treads?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #115
        0x101,
        (
            "#1022F#5P#3SAbsolutely not!#2S\x02\x03",

            "#1002FIn the middle of the biggest war in\x01",
            "Liberl's history, my mother gave her\x01",
            "life to save mine!\x02\x03",

            "And because of that, I chose the path\x01",
            "of a bracer, and now...look at me!\x02\x03",

            "I'm here to stop the crisis YOU caused\x01",
            "and prevent another war from breaking out!\x01",
            "All thanks, in the end, to my mother!\x02\x03",

            "#1005FHell, I'd say you just made my point\x01",
            "for me! People are NOT powerless!\x01",
            "Not against anything!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#1152F#5PPfeh! You're quite good at trite answers,\x01",
            "if nothing else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1002F#5PIf you really, seriously believe people\x01",
            "are powerless...\x02\x03",

            "And you've really convinced yourself\x01",
            "humanity can only be 'saved' by you\x01",
            "turning us into emotionless superbeings...\x02\x03",

            "#1003FThen that makes you really pathetic,\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        "#1153F#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1007F#5PI mean, that'd mean you've never\x01",
            "known the joy of trusting someone or\x01",
            "helping them.\x02\x03",

            "#1003FTo think that your only smug satisfaction\x01",
            "comes from watching people struggle...\x02\x03",

            "That's just... That's too sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        "#1152F#5PHmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1007F#5PBut even if I feel sorry for you,\x01",
            "I am a bracer.\x02\x03",

            "I can't ignore the fact that you're getting\x01",
            "a lot of people involved in your little pity\x01",
            "party.\x02\x03",

            "#1002FSorry, but I'm afraid we're going to have\x01",
            "to stop you. By force.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xF8, 90, 0)
    SetChrChipByIndex(0xF8, 11)
    SetChrSubChip(0xF8, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xF9, 90, 0)
    SetChrChipByIndex(0xF9, 13)
    SetChrSubChip(0xF9, 0)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0x1)
    Fade(500)
    OP_6D(900, 2760, 250, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(91000, 0)
    OP_6E(524, 0)
    SetChrPos(0x8, -1440, 3200, 70, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #122
        0x8,
        (
            "#1152F#6P...\x02\x03",

            "#1154FPheh... You ignorant little girl.\x01",
            "How dare you talk to me like that...?\x02\x03",

            "#1151FVery well, then. The professor would\x01",
            "like for you to prove your theory.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x8, 21)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xBC, 0x0, 0x64)
    SetChrSubChip(0x8, 1)
    Sleep(300)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    Fade(500)
    OP_6D(-16640, 200, 780, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(45000, 0)
    OP_6E(415, 0)
    SetChrPos(0x101, -16570, 200, -110, 90)
    SetChrPos(0xF9, -18040, 200, 590, 90)
    SetChrPos(0xF8, -18430, 200, -1130, 90)
    OP_0D()
    LoadEffect(0x0, "monster\\msc0647a.eff")
    LoadEffect(0x1, "monster\\msc0647b.eff")
    PlayEffect(0x0, 0x0, 0xFF, -16000, 3200, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, -5000, 0)
    Sleep(1200)
    PlayEffect(0x1, 0x1, 0xF8, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xF9, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x390, 0x0, 0x64)
    OP_22(0x10A, 0x0, 0x64)
    Fade(500)
    OP_6B(2160, 500)

    def lambda_58FE():

        label("loc_58FE")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_58FE")

    QueueWorkItem2(0xF8, 1, lambda_58FE)

    def lambda_591B():

        label("loc_591B")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_591B")

    QueueWorkItem2(0xF9, 1, lambda_591B)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5971")

    ChrTalk(    #123
        0x107,
        "#068FWaaaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A9D")

    label("loc_5971")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5994")

    ChrTalk(    #124
        0x105,
        "#1381FAaagh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A9D")

    label("loc_5994")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59BE")

    ChrTalk(    #125
        0x10B,
        "#216FWhoooaaaahhhh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A9D")

    label("loc_59BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59E4")

    ChrTalk(    #126
        0x103,
        "#523FGh, what?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A9D")

    label("loc_59E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A0D")

    ChrTalk(    #127
        0x10F,
        "#172FWhat...in...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A9D")

    label("loc_5A0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A2D")

    ChrTalk(    #128
        0x108,
        "#077FGuh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A9D")

    label("loc_5A2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A57")

    ChrTalk(    #129
        0x104,
        "#039FMmgh! What...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A9D")

    label("loc_5A57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A78")

    ChrTalk(    #130
        0x110,
        "#273FMmph!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A9D")

    label("loc_5A78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A9D")

    ChrTalk(    #131
        0x109,
        "#1070FD'aw, hell!\x02",
    )

    CloseMessageWindow()

    label("loc_5A9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AD3")

    ChrTalk(    #132
        0x106,
        "#055FWhat the...? Can't...move!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6D")

    label("loc_5AD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B07")

    ChrTalk(    #133
        0x109,
        "#1070FHis evil eye! Aw, damn!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6D")

    label("loc_5B07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B2C")

    ChrTalk(    #134
        0x110,
        "#271FHis eyes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6D")

    label("loc_5B2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B6C")

    ChrTalk(    #135
        0x104,
        "#039FSo this is the 'evil eye,' is it...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6D")

    label("loc_5B6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BA1")

    ChrTalk(    #136
        0x108,
        "#077FThe 'evil eye'?! How...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6D")

    label("loc_5BA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BD9")

    ChrTalk(    #137
        0x10F,
        "#172FSomething with...his eyes...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6D")

    label("loc_5BD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C0B")

    ChrTalk(    #138
        0x103,
        "#523FAn actual 'evil eye'?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6D")

    label("loc_5C0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C3E")

    ChrTalk(    #139
        0x10B,
        "#216FHow the hell did he...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6D")

    label("loc_5C3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C6D")

    ChrTalk(    #140
        0x105,
        "#1381FHis eyes...somehow...\x02",
    )

    CloseMessageWindow()

    label("loc_5C6D")


    def lambda_5C73():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C73)
    Sleep(300)

    ChrTalk(    #141
        0x101,
        "#1020F#4PWha...?\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_23(0x10A)

    ChrTalk(    #142
        0x8,
        (
            "#1151F#6PDo be patient for a moment, everyone.\x02\x03",

            "I promise this will be quite a show.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 600)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #143
        0x101,
        "#1005F#6PWhat are you planning, Weissmann?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x8,
        "#1154F#6PJoshua. Forward.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(-7340, 200, 2720, 0)
    OP_67(0, 5250, -10000, 0)
    OP_6B(2730, 0)
    OP_6C(45000, 0)
    OP_6E(453, 0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, -2100, 3200, -950, 270)
    SetChrPos(0x12, -18040, 200, 590, 90)
    SetChrPos(0x11, -18430, 200, -1130, 90)
    SetChrChipByIndex(0x10, 22)
    SetChrChipByIndex(0x11, 11)
    SetChrChipByIndex(0x12, 13)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)

    def lambda_5E30():

        label("loc_5E30")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_5E30")

    QueueWorkItem2(0x11, 1, lambda_5E30)

    def lambda_5E4D():

        label("loc_5E4D")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_5E4D")

    QueueWorkItem2(0x12, 1, lambda_5E4D)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 0)
    OP_0D()

    ChrTalk(    #145
        0x10,
        "#1058F#6P.    .    .\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#1020F#5PJoshua! No!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "#1151F#6PCome, Ms. Bright. Do show me.\x02\x03",

            "You claim humanity can stand against\x01",
            "forces larger than it? Show me proof you\x01",
            "can stand against despair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1005F#5PGh! FINE!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 10)
    OP_7D(0x0, 0x10, 0x32, 0x1F4)
    OP_99(0x10, 0x0, 0x4, 0x5DC)

    def lambda_5F86():
        OP_6D(-15190, 200, -90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F86)

    def lambda_5F9E():
        OP_67(0, 6330, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F9E)

    def lambda_5FB6():
        OP_6B(1880, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5FB6)

    def lambda_5FC6():
        OP_99(0xFE, 0x4, 0x6, 0x9C4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5FC6)

    def lambda_5FD6():
        OP_96(0xFE, 0xFFFFC568, 0xC80, 0xFFFFFEA2, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_5FD6)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    RemoveParty(0x1, 0xFF)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xA, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x10, 0xFF)
    OP_C4(0x0, 0x100)
    Battle(0x2714, 0x300013, 0x0, 0x0, 0xFF)
    OP_C4(0x1, 0x100)
    Return()

    # Function_7_1219 end

    def Function_8_605B(): pass

    label("Function_8_605B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x101, 0x0)
    OP_44(0x10, 0x0)
    Call(0, 3)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x8, 15)
    SetChrPos(0x8, -1440, 3200, 70, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -10370, 200, -800, 135)
    SetChrPos(0x102, -8480, 200, -2730, 315)
    SetChrPos(0xF9, -18810, 200, 970, 90)
    SetChrPos(0xF8, -18420, 200, -1010, 90)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xF8, 11)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 13)
    SetChrSubChip(0xF9, 0)

    def lambda_6114():

        label("loc_6114")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_6114")

    QueueWorkItem2(0xF8, 3, lambda_6114)

    def lambda_6131():

        label("loc_6131")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_6131")

    QueueWorkItem2(0xF9, 3, lambda_6131)
    OP_82(0x81, 0x0)
    OP_82(0x80, 0x0)
    OP_6D(-8440, 200, -1890, 0)
    OP_67(0, 8960, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(90000, 0)
    OP_6E(382, 0)
    LoadEffect(0x1, "Craft\\\\cr161_00.eff")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_61B5"),
        (7, "loc_61C2"),
        (1, "loc_61CF"),
        (SWITCH_DEFAULT, "loc_61DC"),
    )


    label("loc_61B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61DC")

    label("loc_61C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61DC")

    label("loc_61CF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61DC")

    label("loc_61DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6267")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as won (DO NOT USE)\x01",                           # 0
            "Set as endured Joshua's S-Craft (DO NOT USE)\x01",      # 1
            "Set as could not endure it\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)

    label("loc_6267")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_627C"),
        (1, "loc_627F"),
        (2, "loc_63D7"),
        (SWITCH_DEFAULT, "loc_658D"),
    )


    label("loc_627C")

    Jump("loc_658D")

    label("loc_627F")

    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 6)

    def lambda_628F():
        OP_6B(2000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_628F)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #149
        0x102,
        "#1058F#4P.    .    .\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1003F#5PGuh... Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        (
            "#1151F#6PO-ho. Quite an impressive move.\x02\x03",

            "Leaving him with the Divine Blade for\x01",
            "a while seems to have paid off nicely.\x02\x03",

            "#1154FIt does always feel good to see a product\x01",
            "of one's craft honed to an even finer edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1005F#5PYou awful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_658D")

    label("loc_63D7")

    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 5)

    def lambda_63F1():
        OP_6B(2000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63F1)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #153
        0x102,
        "#1058F#4P.    .    .\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1003F#5PGuh... Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x8,
        (
            "#1151F#6PO-ho. Quite an impressive move.\x02\x03",

            "Leaving him with the Divine Blade for\x01",
            "a while seems to have paid off nicely.\x02\x03",

            "#1154FIt does always feel good to see a product\x01",
            "of one's craft honed to an even finer edge.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6521():

        label("loc_6521")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_6521")

    QueueWorkItem2(0x101, 0, lambda_6521)
    Sleep(250)

    def lambda_6543():
        OP_99(0xFE, 0x3, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6543)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x0)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #156
        0x101,
        "#1005F#5PYou awful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_658D")

    label("loc_658D")


    ChrTalk(    #157
        0x8,
        (
            "#1154F#6PAnd now for the climax to our little show.\x02\x03",

            "#1150FJoshua. Seize her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#1020F#5PNo!\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6606():
        OP_6D(-10000, 200, 0, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6606)

    def lambda_661E():
        OP_67(0, 7100, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_661E)

    def lambda_6636():
        OP_6B(2000, 1000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6636)
    SetChrChipByIndex(0x102, 10)
    SetChrSubChip(0x102, 0)
    OP_99(0x102, 0x0, 0x5, 0x9C4)
    SetChrChipByIndex(0x102, 1)
    SetChrSubChip(0x102, 13)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x20)
    OP_7D(0x0, 0x102, 0x32, 0x1F4)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_667F():
        OP_96(0xFE, 0xFFFFD7E2, 0x190, 0xFFFFFB82, 0x1F4, 0x3E80)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_667F)
    Sleep(70)
    OP_22(0x209, 0x0, 0x64)
    SetChrFlags(0x101, 0x800)
    SetChrFlags(0x101, 0x8000)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1)

    def lambda_66CA():
        OP_99(0xFE, 0x0, 0x3, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_66CA)
    WaitChrThread(0x101, 0x0)
    SetChrFlags(0x102, 0x80)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    OP_99(0x101, 0x4, 0x7, 0x9C4)
    WaitChrThread(0x101, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x1E, -11540, 200, 0, 0)

    NpcTalk(    #159
        0x1E,
        "Estelle",
        "#1021F#1PAghh...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6752")

    ChrTalk(    #160
        0x109,
        "#1069FESTELLE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6874")

    label("loc_6752")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6776")

    ChrTalk(    #161
        0x106,
        "#054FESTELLE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6874")

    label("loc_6776")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_679E")

    ChrTalk(    #162
        0x104,
        "#530FNo, Estelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6874")

    label("loc_679E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67C2")

    ChrTalk(    #163
        0x108,
        "#076FEstelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6874")

    label("loc_67C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67E6")

    ChrTalk(    #164
        0x103,
        "#024FESTELLE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6874")

    label("loc_67E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_680A")

    ChrTalk(    #165
        0x107,
        "#065FESTELLE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6874")

    label("loc_680A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6831")

    ChrTalk(    #166
        0x105,
        "#1163FEstelle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6874")

    label("loc_6831")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6855")

    ChrTalk(    #167
        0x10F,
        "#177FEstelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6874")

    label("loc_6855")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6874")

    ChrTalk(    #168
        0x10B,
        "#216FAw no!\x02",
    )

    CloseMessageWindow()

    label("loc_6874")


    def lambda_687A():
        OP_6B(1900, 20000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_687A)
    Sleep(100)
    OP_21()
    OP_1D(0x5B)
    Sleep(500)

    ChrTalk(    #169
        0x8,
        (
            "#1154F#6PAnd thus, the 'strength of humanity'\x01",
            "proves to be nothing more than a house\x01",
            "of cards before a hurricane.\x02\x03",

            "#1150FBut, I am an academic, after all.\x01",
            "I do understand the necessity of proof.\x02\x03",

            "#1151FSo we'll have Joshua provide the final test.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    NpcTalk(    #170
        0x1E,
        "Estelle",
        "#1026F#1PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        (
            "#1154F#6PWhat, indeed?\x01",
            "It will be a simple experiment.\x02\x03",

            "#1150FI am going to have Joshua end your life.\x02\x03",

            "Once you are dead by his hand, I will break\x01",
            "his hypnosis and return him to his senses.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #172
        0x1E,
        "Estelle",
        "#1020F#1P#3SNo... You can't!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#1151F#6POh, I DO wonder what kind of expression\x01",
            "Joshua will have, on seeing you dead at\x01",
            "his feet.\x02\x03",

            "Doesn't it just get your blood pumping?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #174
        0x1E,
        "Estelle",
        (
            "#1022F#1PDon't even think about it!\x02\x03",

            "#1023FIf you do that, Joshua would, he'd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "#1154F#6PYes, this time his heart may just\x01",
            "be crushed to powder.\x02\x03",

            "#1151FIf that happens, however, all I need do\x01",
            "is construct him a new persona.\x02\x03",

            "And then I can offer him the chance to\x01",
            "become human yet again, and observe\x01",
            "the results.\x02\x03",

            "Heh heh... I can hardly wait!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #176
        0x1E,
        "Estelle",
        "#1027F#1PStop... Stop! It's too cruel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#1155F#6PIsn't it?\x02\x03",

            "Now come, Joshua. End her.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x12, 0x13, 0x3E8)
    Sleep(500)

    NpcTalk(    #178
        0x1E,
        "Joshua",
        "#1035F#2P.  .  .\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0x101, 0x7, 0x9, 0x4B0)

    def lambda_6D9F():
        OP_6B(1700, 20000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6D9F)
    Sleep(1000)
    OP_99(0x101, 0x9, 0xB, 0x320)
    Sleep(500)

    NpcTalk(    #179
        0x1E,
        "Estelle",
        (
            "#1027F#1PJoshua...\x02\x03",

            "I'm sorry...\x01",
            "I said I wouldn't die...\x02\x03",

            "I promised I'd...walk with you...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E4D")

    ChrTalk(    #180
        0x10B,
        "#418FJoshua, NO!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EDC")

    label("loc_6E4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E7D")

    ChrTalk(    #181
        0x105,
        "#1169FJoshua, please, no!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EDC")

    label("loc_6E7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EAC")

    ChrTalk(    #182
        0x107,
        "#069FJoshua... NOOOOOOO!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EDC")

    label("loc_6EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EDC")

    ChrTalk(    #183
        0x103,
        "#523FJoshua, snap out of it!\x02",
    )

    CloseMessageWindow()

    label("loc_6EDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F0A")

    ChrTalk(    #184
        0x10F,
        "#177FStop, Joshua! Please!\x02",
    )

    CloseMessageWindow()

    label("loc_6F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F3E")

    ChrTalk(    #185
        0x110,
        "#271FWake up, you fool! Stop!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FDD")

    label("loc_6F3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F6A")

    ChrTalk(    #186
        0x108,
        "#077FWake up, Joshua!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FDD")

    label("loc_6F6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F9D")

    ChrTalk(    #187
        0x104,
        "#530FPlease, Joshua! Awaken!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FDD")

    label("loc_6F9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FDD")

    ChrTalk(    #188
        0x106,
        (
            "#550FJOSHUA!\x01",
            "Wake your dumb ass up and stop!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FDD")


    NpcTalk(    #189
        0x1E,
        "Estelle",
        (
            "#1003F#1PBut I believe in you.\x02\x03",

            "#1025FJoshua...don't give in.\x02\x03",

            "Don't run away from reality...\x01",
            "Even if I die...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x16, 0x17, 0x3E8)
    Sleep(500)
    SetChrPos(0x1E, -11540, 200, -200, 0)

    NpcTalk(    #190
        0x1E,
        "Joshua",
        (
            "#1035F#4PTo be honest, if you did die,\x01",
            "I'm not sure I could face reality.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1E, 0xFFFFFED4, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x2B)
    Sleep(500)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    LoadEffect(0x2, "map\\\\mp009_00.eff")
    PlayEffect(0x0, 0x0, 0x101, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x101, 31)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x102, 0x20)

    def lambda_718B():
        OP_8F(0xFE, 0xFFFFD97C, 0x898, 0x258, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_718B)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(500)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-620, 4500, 40, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(140000, 0)
    OP_6E(446, 0)
    OP_7D(0x0, 0x102, 0x32, 0x1F4)
    SetChrPos(0x102, -1990, 6500, 630, 90)
    SetChrChipByIndex(0x102, 24)
    SetChrSubChip(0x102, 2)
    SetChrPos(0x8, -800, 3200, 500, 270)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 19)
    OP_0D()

    def lambda_7240():
        OP_6D(-620, 3200, 40, 200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7240)

    def lambda_7258():
        OP_6B(1670, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7258)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x80)

    def lambda_7272():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7272)

    def lambda_7284():
        OP_8F(0xFE, 0xFFFFF83A, 0xC80, 0x276, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7284)

    def lambda_729F():
        OP_99(0xFE, 0x3, 0x8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_729F)

    def lambda_72AF():
        OP_99(0xFE, 0x0, 0x5, 0x1194)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_72AF)
    Sleep(300)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0x8, 0, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    def lambda_730F():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_730F)

    def lambda_7329():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_7329)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    Sleep(500)

    def lambda_735F():
        OP_6D(1670, 2700, -700, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_735F)

    def lambda_7377():
        OP_6B(1880, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7377)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_738C():
        OP_96(0xFE, 0xC6C, 0xA8C, 0x316, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_738C)

    def lambda_73AA():
        OP_99(0xFE, 0x5, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_73AA)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x8, 0x2)
    Sleep(500)
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0x102, 0x9, 0xC, 0x5DC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #191
        0x8,
        "#1153F#6PWhat?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x1000)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 22)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_741D():
        OP_96(0xFE, 0xFFFFDEF4, 0xC8, 0xC8, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_741D)
    Sleep(200)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-14300, 200, -110, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(1950, 0)
    OP_6C(135000, 0)
    OP_6E(482, 0)
    WaitChrThread(0x102, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x101, 30)
    ClearChrFlags(0x101, 0x8000)
    OP_0D()
    Sleep(500)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74D5")

    ChrTalk(    #192
        0x107,
        "#064FAh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D2")

    label("loc_74D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74F5")

    ChrTalk(    #193
        0x105,
        "#1164FAh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D2")

    label("loc_74F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7514")

    ChrTalk(    #194
        0x110,
        "#273FMm?\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D2")

    label("loc_7514")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7533")

    ChrTalk(    #195
        0x10B,
        "#213FAh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D2")

    label("loc_7533")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7552")

    ChrTalk(    #196
        0x103,
        "#023FOh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D2")

    label("loc_7552")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7573")

    ChrTalk(    #197
        0x10F,
        "#173FOh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D2")

    label("loc_7573")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7594")

    ChrTalk(    #198
        0x108,
        "#073FOh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D2")

    label("loc_7594")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75B4")

    ChrTalk(    #199
        0x104,
        "#033FOho!\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D2")

    label("loc_75B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75D2")

    ChrTalk(    #200
        0x106,
        "#052FWha--\x02",
    )

    CloseMessageWindow()

    label("loc_75D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_760C")

    ChrTalk(    #201
        0x109,
        (
            "#1060FAwww, yeah!\x01",
            "That's checkmate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_760C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7649")

    ChrTalk(    #202
        0x106,
        "#051FAbout time you snapped out of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_7649")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76A6")

    ChrTalk(    #203
        0x104,
        (
            "#030FThe timing for a dramatic twist\x01",
            "could not have been more fitting!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_76A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76E6")

    ChrTalk(    #204
        0x108,
        (
            "#070FYou were able to break free,\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_76E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7717")

    ChrTalk(    #205
        0x10F,
        "#171FYou broke your curse!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_7717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7754")

    ChrTalk(    #206
        0x103,
        "#020FYou freed yourself! Oh, Joshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_7754")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7786")

    ChrTalk(    #207
        0x10B,
        "#210FYou're back to normal!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_7786")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77C9")

    ChrTalk(    #208
        0x110,
        (
            "#275FSo you were able to break free,\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7801")

    label("loc_77C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7801")

    ChrTalk(    #209
        0x105,
        "#1382FJoshua...are you free at last?\x02",
    )

    CloseMessageWindow()

    label("loc_7801")


    def lambda_7807():
        OP_6D(-9410, 200, 40, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7807)

    def lambda_781F():
        OP_67(0, 5160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_781F)

    def lambda_7837():
        OP_6B(1810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7837)

    def lambda_7847():
        OP_6E(482, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7847)

    def lambda_7857():
        OP_8E(0xFE, 0xFFFFCA72, 0xC8, 0x14, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_7857)
    Sleep(100)

    def lambda_7877():
        OP_8E(0xFE, 0xFFFFC89C, 0xC8, 0x71C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7877)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    def lambda_78A6():

        label("loc_78A6")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_78A6")

    QueueWorkItem2(0x101, 0, lambda_78A6)
    Sleep(250)
    Fade(500)
    SetChrPos(0x101, -11500, 200, 300, 135)
    ClearChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1)
    ClearChrFlags(0x101, 0x800)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0x101, 5)
    OP_0D()

    def lambda_78F8():
        OP_99(0xFE, 0x3, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_78F8)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x0)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #210
        0x101,
        "#1026F#4PJoshua...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x102,
        (
            "#1035F#6PSorry, Estelle.\x02\x03",

            "#1054FI didn't mean to scare you like that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, -1400, 3100, 0, 270)
    SetChrFlags(0x8, 0x800)

    def lambda_79AB():
        OP_6D(-4500, 2000, -2290, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_79AB)

    def lambda_79C3():
        OP_67(0, 2600, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79C3)

    def lambda_79DB():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_79DB)

    def lambda_79EB():
        OP_6E(490, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_79EB)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #212
        0x8,
        (
            "#1153F#6PWhat...? What? This is absurd.\x02\x03",

            "He can't possibly have reclaimed\x01",
            "his will with the--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #213
        0x8,
        "#1157F#6PWait!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-7170, 200, -820, 0)
    OP_67(0, 4380, -10000, 0)
    OP_6B(1760, 0)
    OP_6C(135000, 0)
    OP_6E(490, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #214
        0x8,
        (
            "#1158F#4PThe Stigma! What happened to the\x01",
            "Stigma on your shoulder?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        (
            "#1035F#6POh, yes. That.\x02\x03",

            "#1042FThe Stigma you carved into my\x01",
            "flesh and mind is gone.\x02\x03",

            "Thanks to you, it has been shattered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x8,
        "#1156F#4PBut...HOW?!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-4500, 2000, -2290, 0)
    OP_67(0, 2600, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(135000, 0)
    OP_6E(490, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #217
        0x102,
        (
            "#1042F#2PI had a hypnotic wedge, of sorts, jammed into\x01",
            "the Stigma, keyed to a particular command.\x02\x03",

            "I've been 'poking' at the wedge on my own\x01",
            "since then, getting it ready to shatter the\x01",
            "Stigma the instant someone put pressure on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x8,
        "#1157F#6PWhat?! You...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        "#1026F#2PA...what now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x102,
        (
            "#1040F#2PA wedge. I was afraid I wouldn't be\x01",
            "able to keep our promise, the way\x01",
            "things were going.\x02\x03",

            "So I asked Kevin for a little hypnotic\x01",
            "assistance after we crashed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        "#1004F#2PKevin?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81AE")

    ChrTalk(    #222
        0x109,
        (
            "#1068F#2PAhahaaa... Guilty as charged! Honestly,\x01",
            "I wasn't even sure what to make of his crazy\x01",
            "plan at first.\x02\x03",

            "#1067FIf he'd bet wrong, I dread to think what\x01",
            "could have ended up happening...\x02\x03",

            "#1062FSo, uh, hey! Good job beating the odds there,\x01",
            "J!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x102,
        "#1054F#2PHaha... Thank you, Kevin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        (
            "#1008F#2PWell, uh, haha... Not what I expected,\x01",
            "but I'm not gonna complain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x8,
        (
            "#1157F#6PFather Graham, was it?\x02\x03",

            "I thought you were just a fledgling little\x01",
            "squire, but it seems I underestimated your\x01",
            "bag of cute tricks. A mistake I'll not repeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x109,
        (
            "#1065F#2PI say it's more the guidance of Aidios\x01",
            "than anything.\x02\x03",

            "#1060FI guess I really shouldn't expect you to\x01",
            "get it, what with you turning your back\x01",
            "on the faith an' all.\x02\x03",

            "#1066FBesides, wasn't really my idea to start with!\x02\x03",

            "Someone else gave Joshua the idea,\x01",
            "and I just ran with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x8,
        "#1156F#6PWhat? Who else...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #228
        0x8,
        "#1158F#6PNO! CASSIUS BRIGHT, DAMN YOU!\x02",
    )

    CloseMessageWindow()
    Jump("loc_835F")

    label("loc_81AE")


    ChrTalk(    #229
        0x8,
        (
            "#1152F#6PThis is Kevin Graham's doing, is it?\x02\x03",

            "I thought he was just a fledgling little\x01",
            "squire, but it seems I underestimated his\x01",
            "bag of cute tricks. A mistake I'll not repeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x102,
        (
            "#1035F#2PAt this point, I owe him my freedom and\x01",
            "life.\x02\x03",

            "#1040FOf course, I owe someone else the same\x01",
            "for pointing me in the right direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x8,
        "#1156F#6PWhat? Who else...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #232
        0x8,
        "#1158F#6PNO! CASSIUS BRIGHT, DAMN YOU!\x02",
    )

    CloseMessageWindow()

    label("loc_835F")


    ChrTalk(    #233
        0x101,
        "#1004F#2PDad...?\x02",
    )

    CloseMessageWindow()
    OP_AD(0x2400C5, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #234
        0x101,
        (
            "#1025F#2POh! The letter he gave you before\x01",
            "we got on the Arseille!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x102,
        (
            "#1040F#2PYes. That was why he wanted to make\x01",
            "sure only I read the letter, just in case\x01",
            "anyone was listening in.\x02\x03",

            "#1035F'I suspect your best chance of breaking\x01",
            "the curse lies in Father Kevin's hands.'\x02\x03",

            "'How to use that key is a decision that\x01",
            "must be yours alone to make.'\x02\x03",

            "#1040F'Win your freedom by predicting what\x01",
            "Weissmann will do.'\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8552")

    ChrTalk(    #236
        0x107,
        "#560F#2PWow!\x02",
    )

    CloseMessageWindow()

    label("loc_8552")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8595")

    ChrTalk(    #237
        0x103,
        (
            "#021F#2PHeehee! That's my master,\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8701")

    label("loc_8595")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85DF")

    ChrTalk(    #238
        0x106,
        (
            "#051F#2PHeh...\x01",
            "Yeah, that's the old man,\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8701")

    label("loc_85DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8629")

    ChrTalk(    #239
        0x108,
        (
            "#071F#2PHaha.\x01",
            "Yes, that sounds like Master Cassius.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8701")

    label("loc_8629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8671")

    ChrTalk(    #240
        0x105,
        "#1168F#2PHaha... That's just like General Bright.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8701")

    label("loc_8671")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86BC")

    ChrTalk(    #241
        0x10F,
        (
            "#171FHaha...\x01",
            "Just as you'd expect of General Bright.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8701")

    label("loc_86BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8701")

    ChrTalk(    #242
        0x104,
        (
            "#031F#2PI'd expect no less out of\x01",
            "Cassius Bright!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8701")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8742")

    ChrTalk(    #243
        0x110,
        "#275FHeh, most impressive, General Bright.\x02",
    )

    CloseMessageWindow()
    Jump("loc_878A")

    label("loc_8742")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_878A")

    ChrTalk(    #244
        0x10B,
        (
            "#210F#2PWhat in the heck?\x01",
            "Well, that works, I guess!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_878A")


    ChrTalk(    #245
        0x101,
        (
            "#1016F#2POh, for crying out...\x01",
            "Dad could've dropped me a HINT\x01",
            "about this, at least!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x8,
        "#1157F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x102,
        (
            "#1043F#2PHonestly, I'd been worried about it\x01",
            "for a long time.\x02\x03",

            "I kept wondering what you would\x01",
            "make me do if you took control of\x01",
            "me again.\x02\x03",

            "#1035FAnd so, knowing you, I decided to\x01",
            "bet everything on one idea.\x02\x03",

            "That you couldn't possibly resist\x01",
            "ordering me to do the one thing I\x01",
            "feared the most.\x02\x03",

            "#1042FAnd sure enough, you ordered it...\x01",
            "and that broke the Stigma.\x02\x03",

            "I'm finally...completely free of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        "#1025F#2PJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x8,
        (
            "#1157F#6P...\x01",
            "You foolish little child.\x02\x03",

            "If you had just obeyed me, you could\x01",
            "have aspired to such heights.\x02\x03",

            "I could have advanced you in ways\x01",
            "you cannot even dream of!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x102,
        (
            "#1035F#2PMuch like how Estelle turned you down\x01",
            "once...I really have no interest in any of\x01",
            "that.\x02\x03",

            "#1040FBesides, if I've learned anything in this\x01",
            "whole journey, it's that one's path in life\x01",
            "isn't given by someone else.\x02\x03",

            "It's something you find WITH others as\x01",
            "you search for it, no matter how dark\x01",
            "your surroundings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x8,
        (
            "#1151F#6PHahah! Absurd!\x02\x03",

            "The history of man is stained with\x01",
            "the blood of fools who tried finding\x01",
            "your 'path'!\x02\x03",

            "Without a guiding light to shine on\x01",
            "that road, they shall remain lost!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x102,
        (
            "#1042F#2PYou're wrong!\x02\x03",

            "We use the light we each give off\x01",
            "to find our way together!\x02\x03",

            "#1046FThat is how we found our way here,\x01",
            "through all your cynical traps!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x101,
        "#1006F#2PThat's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x8,
        (
            "#1154F#6PHeh... Heheh...\x01",
            "You do like your speeches, don't you,\x01",
            "you shambling wreck of an Enforcer.\x02\x03",

            "#1151FShow me, then.\x02\x03",

            "Show me this light you claim will guide\x01",
            "you through the darkness.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 19)
    OP_99(0x8, 0x0, 0x3, 0x5DC)
    OP_22(0xD8, 0x0, 0x64)
    OP_99(0x8, 0x4, 0x6, 0x5DC)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(370, 3800, 0, 0)
    OP_67(0, 3590, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(90000, 0)
    OP_6E(437, 0)
    SetChrPos(0x8, -1400, 3200, 0, 270)
    ClearChrFlags(0x8, 0x800)
    OP_21()
    OP_1D(0x3A)
    Sleep(500)

    def lambda_8EB1():
        OP_6D(370, 3600, 0, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8EB1)

    def lambda_8EC9():
        OP_6B(2100, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EC9)
    OP_43(0x19, 0x0, 0x0, 0x14)
    Sleep(120)
    OP_43(0x1B, 0x0, 0x0, 0x16)
    Sleep(130)
    OP_43(0x1C, 0x0, 0x0, 0x17)
    Sleep(110)
    OP_43(0x1A, 0x0, 0x0, 0x15)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x1B, 0x0)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_82(0x0, 0x2)
    SetChrPos(0x102, -10900, 200, 800, 90)
    SetChrPos(0x101, -10900, 200, -820, 90)
    SetChrPos(0xF9, -13200, 200, 1100, 90)
    SetChrPos(0xF8, -13200, 200, -1100, 90)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 22)
    SetChrChipByIndex(0xF8, 11)
    SetChrChipByIndex(0xF9, 13)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_99(0x8, 0x6, 0x0, 0x5DC)
    Sleep(500)

    ChrTalk(    #255
        0x8,
        (
            "#1155F#5PAnd I shall show you in turn...\x02\x03",

            "...the blinding light of a loyal servant of\x01",
            "the Grandmaster! The power of the Faceless,\x01",
            "one of the Anguis!\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9047():
        OP_6D(-6310, 2180, 60, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9047)

    def lambda_905F():
        OP_67(0, 2840, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_905F)

    def lambda_9077():
        OP_6B(2950, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9077)

    def lambda_9087():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9087)

    def lambda_9097():
        OP_6E(441, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9097)
    WaitChrThread(0x101, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #256
        0x101,
        "#1005F#2PBRING IT ON!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x102,
        "#1046F#5PThe one being blinded here is you!\x02",
    )

    CloseMessageWindow()

    def lambda_9101():
        OP_6D(-3100, 2200, -20, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9101)

    def lambda_9119():
        OP_67(0, 2950, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9119)

    def lambda_9131():
        OP_6B(2050, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9131)

    def lambda_9141():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9141)

    def lambda_915C():
        OP_8F(0xFE, 0xFFFFEE6C, 0x898, 0x21C, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_915C)
    Sleep(10)

    def lambda_917C():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_917C)

    def lambda_9197():
        OP_8F(0xFE, 0xFFFFEE6C, 0x898, 0xFFFFFDE4, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_9197)
    Sleep(10)

    def lambda_91B7():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_91B7)

    def lambda_91D2():
        OP_8F(0xFE, 0xFFFFEE6C, 0x6A4, 0x21C, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_91D2)
    Sleep(10)

    def lambda_91F2():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_91F2)

    def lambda_920D():
        OP_8F(0xFE, 0xFFFFEE6C, 0x6A4, 0xFFFFFDE4, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_920D)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_BB(0x1, 0x1, 0x1C)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0xA, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x8, 0xFE, 0x0)
    OP_31(0xE, 0xFE, 0x0)
    OP_31(0xF, 0xFE, 0x0)
    Battle(0x459, 0x30000C, 0x0, 0x0, 0xFF)
    Return()

    # Function_8_605B end

    def Function_9_92A2(): pass

    label("Function_9_92A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x19, 0x0)
    OP_44(0x1A, 0x0)
    OP_44(0x1B, 0x0)
    OP_44(0x1C, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    Call(0, 4)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1400, 3200, 0, 270)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x101, -8200, 200, -700, 90)
    SetChrPos(0x102, -8200, 200, 700, 90)
    SetChrPos(0xF8, -9600, 200, -800, 90)
    SetChrPos(0xF9, -9600, 200, 800, 90)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0xF8, 11)
    SetChrChipByIndex(0xF9, 13)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-5400, 3000, -70, 0)
    OP_67(0, 2500, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(44000, 0)
    OP_6E(478, 0)
    FadeToBright(1000, 0)
    OP_6B(2500, 2000)
    OP_0D()

    ChrTalk(    #258
        0x8,
        (
            "#1153F#4POh, my. What a shock.\x02\x03",

            "To think that you would be so\x01",
            "damned tenacious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        (
            "#1022F#5P*pant* *pant*\x02\x03",

            "#1006FHey, 'Professor,' about time you dropped\x01",
            "that 'holier than thou' act.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94BD")

    ChrTalk(    #260
        0x10B,
        "#210F#5PSOMEBODY'S feeling the heat!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9737")

    label("loc_94BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_950B")

    ChrTalk(    #261
        0x103,
        (
            "#027F#5PLosing a bit of that insane confidence,\x01",
            "are we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9737")

    label("loc_950B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9542")

    ChrTalk(    #262
        0x110,
        "#277F#5PHmph. Losing confidence?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9737")

    label("loc_9542")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_958D")

    ChrTalk(    #263
        0x106,
        (
            "#051F#5PHeh. Someone knows he's up\x01",
            "against the wall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9737")

    label("loc_958D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95E8")

    ChrTalk(    #264
        0x104,
        (
            "#035F#5PYour confidence drains away like sand\x01",
            "in a sieve, Weissmann.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9737")

    label("loc_95E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_962D")

    ChrTalk(    #265
        0x10F,
        (
            "#170FBeginning to lose your confidence,\x01",
            "fiend?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9737")

    label("loc_962D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_966C")

    ChrTalk(    #266
        0x108,
        "#070F#1PHmm. Realizing the end has come?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9737")

    label("loc_966C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96D7")

    ChrTalk(    #267
        0x105,
        (
            "#1167F#5PYour confidence drains away...\x01",
            "because you know this is the end,\x01",
            "don't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9737")

    label("loc_96D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9737")

    ChrTalk(    #268
        0x109,
        (
            "#1060F#5PFeelin' a little nervous, starin'\x01",
            "justice right in the face, Georg?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9737")


    ChrTalk(    #269
        0x8,
        (
            "#1154F#4PHeh heh. Pathetic.\x02\x03",

            "#1155FYou haven't even realized you're\x01",
            "standing on your graves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        "#1004F#5PWhat?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x20)

    def lambda_980D():
        OP_8F(0xFE, 0xFFFFFA88, 0x1194, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_980D)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    OP_44(0x8, 0x1)
    SetChrPos(0x8, 8150, 4000, 0, 270)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(8119, 2800, 0, 0)
    OP_67(0, 3340, -10000, 0)
    OP_6B(2130, 0)
    OP_6C(90000, 0)
    OP_6E(478, 0)
    OP_0D()

    def lambda_9894():
        OP_8F(0xFE, 0x1FD6, 0xA14, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9894)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x101, 0x2)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #271
        0x101,
        "#1020FAh#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x102,
        "#1042F#5PWeissmann, what are you doing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x8,
        (
            "#1155F#6PI had intended to offer it to the Grandmaster\x01",
            "like this, but I must change my plans.\x02\x03",

            "It's time you realized just what it means\x01",
            "to oppose me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_DB()
    OP_1D(0x70)
    Sleep(500)
    LoadEffect(0x0, "map\\mp062_02.eff")
    LoadEffect(0x1, "map\\mp098_00.eff")
    Fade(250)
    OP_E8(0xD0, 0x7, 0x0, 0x0)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 18)
    OP_0D()
    Sleep(500)

    def lambda_99FF():
        OP_6D(8119, 9660, 0, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_99FF)

    def lambda_9A17():
        OP_67(0, 4930, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A17)

    def lambda_9A2F():
        OP_6B(1800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A2F)

    def lambda_9A3F():

        label("loc_9A3F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_9A3F")

    QueueWorkItem2(0x8, 1, lambda_9A3F)
    OP_22(0x145, 0x0, 0x64)

    def lambda_9A57():
        OP_8F(0xFE, 0x1FD6, 0x2486, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9A57)
    Sleep(200)

    def lambda_9A77():
        OP_8F(0xFE, 0x1FD6, 0x2486, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9A77)
    Sleep(400)

    def lambda_9A97():
        OP_8F(0xFE, 0x1FD6, 0x2486, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9A97)
    Sleep(700)

    def lambda_9AB7():
        OP_8F(0xFE, 0x1FD6, 0x2486, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9AB7)
    Sleep(400)

    def lambda_9AD7():
        OP_8F(0xFE, 0x1FD6, 0x2486, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9AD7)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(1500)

    def lambda_9B06():
        OP_6D(14380, 2700, 360, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9B06)

    def lambda_9B1E():
        OP_67(0, 9500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B1E)

    def lambda_9B36():
        OP_6B(3380, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B36)
    PlayEffect(0x0, 0x0, 0xFF, 8031, 5100, 92, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x0, 0x64)
    Sleep(2500)

    def lambda_9BBA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9BBA)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_6D(8180, 2580, 200, 0)
    OP_67(0, 593740, -10000, 0)
    OP_6B(120, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    def lambda_9C27():
        OP_6D(8039, 2580, 320, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9C27)

    def lambda_9C3F():
        OP_6B(180, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C3F)
    WaitChrThread(0x101, 0x0)
    Sleep(1500)
    Fade(500)
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(-7680, 200, 820, 0)
    OP_67(0, 7710, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)
    OP_0D()
    Sleep(300)
    OP_DC()

    ChrTalk(    #274
        0x101,
        "#1020F#5PWhat in the...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x102,
        "#1044F#6PHe wouldn't...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D78")

    ChrTalk(    #276
        0x109,
        (
            "#1069F#1POh, no... No no no! Don't FUSE with\x01",
            "the Aureole, you heretical maniac!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FFF")

    label("loc_9D78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DB5")

    ChrTalk(    #277
        0x105,
        "#1163F#1PHe's fusing with the Aureole!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FFF")

    label("loc_9DB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E05")

    ChrTalk(    #278
        0x103,
        (
            "#023F#1PHe's...FUSING with the Aureole?!\x01",
            "He can do that?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FFF")

    label("loc_9E05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E98")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E5C")

    ChrTalk(    #279
        0x108,
        (
            "#072F#1PImpossible... He's fusing with the\x01",
            "Aureole!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E95")

    label("loc_9E5C")


    ChrTalk(    #280
        0x108,
        (
            "#072F#3PImpossible... He's fusing with the\x01",
            "Aureole!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E95")

    Jump("loc_9FFF")

    label("loc_9E98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9ED1")

    ChrTalk(    #281
        0x10F,
        "#172FHe's fusing with the Aureole!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FFF")

    label("loc_9ED1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F25")

    ChrTalk(    #282
        0x104,
        (
            "#033F#1PHe can't be... He would become\x01",
            "one with the Aureole?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FFF")

    label("loc_9F25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F78")

    ChrTalk(    #283
        0x106,
        (
            "#055F#1PWhat in the hell?!\x01",
            "He's MERGING with the damn thing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FFF")

    label("loc_9F78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FC0")

    ChrTalk(    #284
        0x107,
        "#065F#1PN-No way... He's fusing with the Aureole!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9FFF")

    label("loc_9FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FFF")

    ChrTalk(    #285
        0x110,
        "#273FHe's... What? Fusing with the Aureole?\x02",
    )

    CloseMessageWindow()

    label("loc_9FFF")

    OP_DB()
    Sleep(100)
    Fade(500)
    OP_82(0x82, 0x0)
    OP_6D(14340, 2700, 350, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4010, 0)
    OP_6C(90000, 0)
    OP_6E(372, 0)
    PlayEffect(0x1, 0x1, 0x8, 0, 0, 0, 0, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_A085():
        OP_6B(2600, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A085)
    OP_22(0x146, 0x0, 0x64)
    OP_22(0x147, 0x0, 0x64)
    Sleep(5000)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x8, 0x1)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 9580, 5500, 0, 270)
    OP_A1(0x8, 0x0)
    OP_72(0x0, 0x4)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 171)
    OP_70(0x0, 0xD2)
    SetChrPos(0x101, -8200, 200, -700, 90)
    SetChrPos(0x102, -8200, 200, 700, 90)
    SetChrPos(0xF8, -9600, 200, -800, 90)
    SetChrPos(0xF9, -9600, 200, 800, 90)
    Sleep(4000)
    OP_6D(3940, 6130, -250, 0)
    OP_67(0, 3440, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(269000, 0)
    OP_6E(502, 0)
    FadeToBright(1000, 16777215)
    OP_0D()
    Sleep(1000)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    OP_6D(15590, 3120, 1900, 0)
    OP_67(0, 3150, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(75000, 0)
    OP_6E(494, 0)
    FadeToBright(500, 16777215)
    OP_0D()
    Sleep(1000)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    OP_22(0x149, 0x0, 0x64)
    OP_6D(11650, 9940, -380, 0)
    OP_67(0, 4420, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(117000, 0)
    OP_6E(492, 0)
    FadeToBright(500, 16777215)
    OP_0D()
    Sleep(1000)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    OP_6D(-8520, 200, 0, 0)
    OP_67(0, 4500, -10000, 0)
    OP_6B(1540, 0)
    OP_6C(90000, 0)
    OP_6E(665, 0)
    FadeToBright(500, 16777215)
    Sleep(500)

    def lambda_A3E0():
        OP_6D(13450, 8300, 0, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A3E0)

    def lambda_A3F8():
        OP_67(0, 2410, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A3F8)

    def lambda_A410():
        OP_6B(2300, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A410)

    def lambda_A420():
        OP_6E(600, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A420)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x101, -1810, 3200, -920, 90)
    SetChrPos(0x102, -1810, 3200, 920, 90)
    SetChrPos(0xF8, -2800, 2700, -940, 90)
    SetChrPos(0xF9, -2800, 2700, 940, 90)
    Sleep(500)

    def lambda_A47E():
        OP_6D(13450, 8500, 0, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A47E)

    def lambda_A496():
        OP_67(0, 290, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A496)

    def lambda_A4AE():
        OP_6B(2200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A4AE)
    OP_DC()

    ChrTalk(    #286
        0x101,
        "#1020F#5PHow's that even...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A50C")

    ChrTalk(    #287
        0x10B,
        "#216FWhat. In. The. HELL?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6BA")

    label("loc_A50C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A536")

    ChrTalk(    #288
        0x107,
        "#065FWhat IS that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6BA")

    label("loc_A536")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A557")

    ChrTalk(    #289
        0x110,
        "#270FHmph.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6BA")

    label("loc_A557")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A59E")

    ChrTalk(    #290
        0x106,
        (
            "#055FYou are so beyond kidding me\x01",
            "at this point!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6BA")

    label("loc_A59E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A5E4")

    ChrTalk(    #291
        0x104,
        (
            "#039FThis is getting more absurd by\x01",
            "the minute!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6BA")

    label("loc_A5E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A60B")

    ChrTalk(    #292
        0x108,
        "#077FImpossible!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6BA")

    label("loc_A60B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A63D")

    ChrTalk(    #293
        0x103,
        "#523FBy all that's holy...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6BA")

    label("loc_A63D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A688")

    ChrTalk(    #294
        0x105,
        (
            "#1163FIt can't be...\x01",
            "What has he done to himself...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6BA")

    label("loc_A688")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A6BA")

    ChrTalk(    #295
        0x10F,
        "#173FHow could he possibly...?\x02",
    )

    CloseMessageWindow()

    label("loc_A6BA")


    ChrTalk(    #296
        0x102,
        (
            "#1042F#5PThis overwhelming power!\x01",
            "Can...barely stand...\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x20)
    OP_6F(0x0, 131)
    OP_70(0x0, 0xAA)
    OP_22(0x148, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 11)
    OP_70(0x0, 0x32)
    Sleep(1000)
    SetMessageWindowPos(180, 260, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #297
        (
            "\x07\x05Keh-heh-heh... Oh, this sensation...\x01",
            "Even better than I'd imagined...\x02\x03",

            "Shall we experiment, then?\x02\x03",

            "The power of apotheosis, unflinching reason,\x01",
            "indomitable intellect, guiding humanity to\x01",
            "the future!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    WaitChrThread(0x101, 0x0)
    OP_A2(0x2298)
    Battle(0x465, 0x300014, 0x0, 0x0, 0xFF)
    OP_A3(0x2298)
    Return()

    # Function_9_92A2 end

    def Function_10_A836(): pass

    label("Function_10_A836")

    OP_A2(0x2)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x112), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A3(0x2)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 5)
    SetChrPos(0x101, -8200, 200, -700, 90)
    SetChrPos(0x102, -8200, 200, 700, 90)
    SetChrPos(0xF8, -9600, 200, -800, 90)
    SetChrPos(0xF9, -9600, 200, 800, 90)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0xF8, 15)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 3)
    SetChrSubChip(0x102, 3)
    SetChrSubChip(0xF8, 3)
    SetChrSubChip(0xF9, 3)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x88, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 9580, 5500, 0, 270)
    OP_A1(0x8, 0x0)
    OP_72(0x0, 0x4)
    OP_6D(-8410, 200, -30, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(45000, 0)
    OP_6E(466, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0xA, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x8, 0xFE, 0x0)
    OP_31(0xE, 0xFE, 0x0)
    OP_31(0xF, 0xFE, 0x0)
    OP_22(0x149, 0x0, 0x64)
    FadeToBright(1000, 0)

    def lambda_A9DF():
        OP_6D(12800, 7190, 1790, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A9DF)

    def lambda_A9F7():
        OP_67(0, 2980, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A9F7)

    def lambda_AA0F():
        OP_6B(2720, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AA0F)

    def lambda_AA1F():
        OP_6C(69000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AA1F)

    def lambda_AA2F():
        OP_6E(466, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA2F)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    SetMessageWindowPos(220, 240, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #298
        (
            "\x07\x05There. A lesson learned, I think.\x02\x03",

            "A lesson in real power.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #299
        0x101,
        (
            "#1020F#2PThis is nuts!\x02\x03",

            "Our attacks aren't hitting him at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x102,
        (
            "#1047F#2PHe's got some kind of barrier up!\x02\x03",

            "But if it's negating even our arts\x01",
            "and our best techniques...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 240, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #301
        (
            "\x07\x05Learn, children. The Aureole is the\x01",
            "treasure of Space.\x02\x03",

            "One of its very, very many powers is\x01",
            "forming an absolute barrier, incomparable\x01",
            "to simple orbal arts.\x02\x03",

            "You cannot even touch me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    LoadEffect(0x0, "monster\\msc0647a.eff")
    LoadEffect(0x1, "monster\\msc0647b.eff")
    Fade(500)
    OP_6D(-7000, 200, 1060, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(45000, 0)
    OP_6E(466, 0)
    OP_0D()
    PlayEffect(0x0, 0x0, 0xFF, -5200, 3000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1200)
    PlayEffect(0x1, 0x1, 0x101, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x102, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0xF8, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0xF9, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x390, 0x0, 0x64)
    OP_22(0x10A, 0x0, 0x64)
    Fade(500)
    OP_6B(1800, 500)

    def lambda_ADD1():

        label("loc_ADD1")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_ADD1")

    QueueWorkItem2(0x101, 3, lambda_ADD1)

    def lambda_ADEE():

        label("loc_ADEE")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_ADEE")

    QueueWorkItem2(0x102, 3, lambda_ADEE)

    def lambda_AE0B():

        label("loc_AE0B")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_AE0B")

    QueueWorkItem2(0xF8, 3, lambda_AE0B)

    def lambda_AE28():

        label("loc_AE28")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
        OP_48()
        Jump("loc_AE28")

    QueueWorkItem2(0xF9, 3, lambda_AE28)
    Sleep(1500)

    ChrTalk(    #302
        0x101,
        "#1021F#5PGyah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AE7C")

    ChrTalk(    #303
        0x107,
        "#068F#5PAaaaaah!\x02",
    )

    CloseMessageWindow()

    label("loc_AE7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AEAF")

    ChrTalk(    #304
        0x10B,
        "#216F#5PGnerk, not again...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AECE")

    label("loc_AEAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AECE")

    ChrTalk(    #305
        0x10F,
        "#175F#5PGh!\x02",
    )

    CloseMessageWindow()

    label("loc_AECE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF01")

    ChrTalk(    #306
        0x109,
        "#1070F#5PThe evil eye AGAIN!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF2B")

    label("loc_AF01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF2B")

    ChrTalk(    #307
        0x105,
        "#1381F#5PThe evil eye!\x02",
    )

    CloseMessageWindow()

    label("loc_AF2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF5D")

    ChrTalk(    #308
        0x103,
        "#523F#5PYou twisted sadist!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF96")

    label("loc_AF5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF96")

    ChrTalk(    #309
        0x106,
        "#057F#5PYou sick, twisted son of a...\x02",
    )

    CloseMessageWindow()

    label("loc_AF96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFD5")

    ChrTalk(    #310
        0x110,
        "#271F#5PYou dare toy with me like this?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B00E")

    label("loc_AFD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B00E")

    ChrTalk(    #311
        0x108,
        "#077F#5PYou don't give up, you do...?\x02",
    )

    CloseMessageWindow()

    label("loc_B00E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B038")

    ChrTalk(    #312
        0x104,
        "#039F#5PMy...goodness.\x02",
    )

    CloseMessageWindow()

    label("loc_B038")


    ChrTalk(    #313
        0x102,
        "#1038F#5P#6PWeissmann...let them go.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_23(0x10A)
    OP_6D(12800, 7190, 1790, 0)
    OP_67(0, 2980, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(69000, 0)
    OP_6E(466, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(220, 240, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #314
        (
            "\x07\x05Those eyes. Magnificent. You may be\x01",
            "a wreck of an Enforcer, but, oh, what a\x01",
            "waste it would be to kill you.\x02\x03",

            "I would much prefer to etch another\x01",
            "Stigma into the depths of your mind.\x02\x03",

            "Just as before, I'll give you a renewed\x01",
            "sense of hope, then tear it out by the\x01",
            "roots and leave you writhing!\x02\x03",

            "Nothing pleases me more than to see\x01",
            "that shift in your expression from hope\x01",
            "to despair... I do so look forward to it!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 280)
    OP_70(0x1, 0x12C)
    OP_72(0x1, 0x4)
    OP_CF(0x9, 0x1, "Frame143_on_head")
    OP_A1(0x20, 0x1)
    SetChrPos(0x20, 4500, 20000, 8200, 160)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 280)
    OP_70(0x1, 0x12C)
    SetChrChipByIndex(0x9, 20)
    SetChrSubChip(0x9, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x1000)
    SetMessageWindowPos(50, 75, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #315
        (
            "\x07\x00I can't believe this.\x02\x03",

            "Forget 'bad taste.' The only word\x01",
            "for you at this point is 'sick.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0x3E8)

    ChrTalk(    #316
        0x101,
        "#1020F#2PWho...?!\x02",
    )

    CloseMessageWindow()
    OP_21()
    OP_59()
    OP_1D(0x7B)
    Sleep(1000)
    OP_22(0x158, 0x0, 0x64)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(5800, 15000, 6210, 0)
    OP_67(0, 5430, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(332000, 0)
    OP_6E(513, 0)
    OP_0D()

    def lambda_B3F3():
        OP_8F(0xFE, 0x1194, 0xBB8, 0x2008, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_B3F3)

    def lambda_B40E():
        OP_6D(3430, 5000, 11850, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B40E)

    def lambda_B426():
        OP_67(0, 3440, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B426)

    def lambda_B43E():
        OP_6B(2150, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B43E)

    def lambda_B44E():
        OP_6C(348000, 1200)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B44E)

    def lambda_B45E():
        OP_6E(513, 1200)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B45E)
    OP_71(0x0, 0x4)
    Sleep(400)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 300)
    OP_70(0x1, 0x136)
    WaitChrThread(0x20, 0x1)
    OP_23(0x158)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x514)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x14)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #317
        0x101,
        "#1004F#2POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x102,
        "#1044F#2PLoewe!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_72(0x0, 0x4)
    OP_6D(13040, 2700, -4200, 0)
    OP_67(0, 4450, -10000, 0)
    OP_6B(3730, 0)
    OP_6C(146000, 0)
    OP_6E(588, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrPos(0x101, -10920, 200, -19120, 90)
    SetChrPos(0x102, -10920, 200, -19120, 90)
    SetChrPos(0xF8, -10920, 200, -19120, 90)
    SetChrPos(0xF9, -10920, 200, -19120, 90)
    OP_0D()

    def lambda_B595():
        OP_6D(6380, 6000, -2730, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B595)

    def lambda_B5AD():
        OP_67(0, 2760, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5AD)

    def lambda_B5C5():
        OP_6B(3560, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B5C5)

    def lambda_B5D5():
        OP_6C(185000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B5D5)

    def lambda_B5E5():
        OP_6E(553, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B5E5)
    LoadEffect(0x0, "map\\mp095_00.eff")
    LoadEffect(0x2, "map\\mp100_00.eff")
    LoadEffect(0x3, "monster\\ms31004a.eff")
    LoadEffect(0x4, "map\\mp099_00.eff")
    OP_72(0x1, 0x20)
    OP_D8(0x1, 0x1F4)
    OP_6F(0x1, 880)
    OP_70(0x1, 0x3AC)
    OP_22(0x142, 0x0, 0x64)
    Sleep(2000)
    Play3DEffect(0x0, 0x0, 0x1, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0xAA, 0x0, 0xFFEC, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(50)
    OP_22(0x143, 0x0, 0x64)
    Play3DEffect(0x0, 0x1, 0x1, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0xA0, 0x0, 0xFFFB, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_73(0x1)
    WaitChrThread(0x101, 0x1)
    PlayEffect(0x3, 0x2, 0x8, 0, 0, 0, 0, 0, 0, 11000, 21000, 11000, 0xFF, 0, 0, 0, 0)
    Fade(500)

    def lambda_B722():
        OP_6B(2760, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B722)
    OP_D8(0x1, 0x1F4)
    OP_B0(0x1, 0x14)
    OP_6F(0x1, 1070)
    OP_70(0x1, 0x438)
    OP_73(0x1)
    WaitChrThread(0x101, 0x0)
    OP_82(0x0, 0x0)
    OP_7C(0x258, 0x258, 0xBB8, 0x1F4)
    PlayEffect(0x2, 0x3, 0xFF, 7000, 6800, 2700, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x8, 0, 1500, 0, 40, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x20, 0x3, 0x0, 0xF)
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0xF)
    OP_6F(0x1, 1080)
    OP_70(0x1, 0x43D)
    OP_22(0x14A, 0x0, 0x64)

    def lambda_B7F1():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_B7F1)
    WaitChrThread(0x101, 0x1)

    def lambda_B804():
        OP_8C(0xFE, 335, 50)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_B804)
    WaitChrThread(0x8, 0x0)
    Sleep(500)

    def lambda_B81C():

        label("loc_B81C")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x64)
        OP_48()
        Jump("loc_B81C")

    QueueWorkItem2(0x101, 0, lambda_B81C)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #319
        (
            "\x07\x05Hmph! I suppose I should have\x01",
            "finished you off.\x02\x03",

            "Though really, Loewe, what ARE\x01",
            "you planning on doing?\x02\x03",

            "Not even your dragon can break\x01",
            "the Aureole's barrier.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #320
        0x9,
        (
            "#124F#4PI suppose it can't.\x02\x03",

            "#121FI did have a question for you,\x01",
            "though, Weissmann.\x02\x03",

            "Just how involved were you in Hamel?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -3840, 200, 11780, 135)
    SetChrPos(0x102, -2670, 200, 13060, 135)
    SetChrPos(0xF8, -4660, 200, 13340, 135)
    SetChrPos(0xF9, -3540, 200, 14580, 135)

    ChrTalk(    #321
        0x102,
        "#1044F#1PWait, what?!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #322
        (
            "\x07\x05Now what a thing to accuse me of!\x02\x03",

            "That was purely the fault of the\x01",
            "Empire's hawks, no?\x02\x03",

            "Why would you ever think I would\x01",
            "be involved?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #323
        0x9,
        (
            "#121F#4PBecause you're a snake.\x02\x03",

            "#124FYou appear before people in their moments\x01",
            "of weakness and whisper plans into their\x01",
            "ears that lead to their destruction.\x02\x03",

            "And, in doing so, you achieve your goals\x01",
            "without ever dirtying your belly.\x02\x03",

            "#120F...That's just your way of doing things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x102,
        "#1042F#1PNo... He... Would he...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x9,
        (
            "#124F#4PThe ringleaders of the hawks were nothing more\x01",
            "than political losers who had nowhere else to go.\x02\x03",

            "There were a few questions I couldn't answer\x01",
            "at first, but if even the war ten years ago was \x01",
            "part of your plan...\x02\x03",

            "#120FIt then occurred to me. Everything made sense.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 150, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #326
        (
            "\x07\x05Heh heh heh... I see.\x02\x03",

            "It is largely as you surmise.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #327
        0x101,
        "#1020F#1PWH-WH-WHAT?!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #328
        (
            "\x07\x05Of course, really, all I did was introduce\x01",
            "them to a band of jaeger dropouts I knew\x01",
            "and put the name 'Hamel' in their ears.\x02\x03",

            "Just doing that was enough to push things\x01",
            "to war in the blink of an eye!\x02\x03",

            "Heh heh... Simply one more testament to\x01",
            "the sinful nature of men.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BEDC")

    ChrTalk(    #329
        0x106,
        (
            "#550F#1PYou son of a bitch...\x02\x03",

            "Mischa died just so you could prove\x01",
            "a goddamn POINT?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF11")

    ChrTalk(    #330
        0x107,
        "#069F#1PAwful... That's so awful!\x02",
    )

    CloseMessageWindow()

    label("loc_BF11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF75")

    ChrTalk(    #331
        0x104,
        (
            "#039F#1PAstounding. Do you truly seek to be\x01",
            "the foulest man in history, monster?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFBC")

    ChrTalk(    #332
        0x10F,
        (
            "#177F#1PHow...\x01",
            "How many died...just because of you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C00F")

    ChrTalk(    #333
        0x105,
        (
            "#1162F#1PWhat you've done is...\x01",
            "It's unforgivable, you monster!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C00F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C068")

    ChrTalk(    #334
        0x103,
        (
            "#523F#1PYou unbelievable monster...\x01",
            "Gehenna will be too kind for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C068")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0AD")

    ChrTalk(    #335
        0x108,
        (
            "#077F#1PKarma's wheel will spin for you,\x01",
            "monster.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0E9")

    ChrTalk(    #336
        0x10B,
        "#216F#1PPeople like this actually EXIST?\x02",
    )

    CloseMessageWindow()

    label("loc_C0E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C135")

    ChrTalk(    #337
        0x110,
        (
            "#276F#1PClearly you should have met\x01",
            "your death long ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C135")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C173")

    ChrTalk(    #338
        0x109,
        "#1063F#1POne more sin for the pile, eh...?\x02",
    )

    CloseMessageWindow()

    label("loc_C173")


    ChrTalk(    #339
        0x101,
        "#1027F#1PI... I think I'm gonna be sick...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x9,
        "#124F#4PI see. Essentially as I thought, then.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(75, 150, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #341
        (
            "\x07\x05You're taking this rather well.\x02\x03",

            "Personally, I was hoping you'd be a bit\x01",
            "more resentful.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #342
        0x9,
        (
            "#1430F#4PHah. Have you forgotten?\x01",
            "I've long since learned to stay my anger.\x02\x03",

            "#123FHowever, you knocked me out from\x01",
            "behind back there. That is an insult the\x01",
            "Bladelord cannot abide.\x02\x03",

            "That, alone, I shall be paying back in full.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 150, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #343
        "\x07\x05What...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    LoadEffect(0x6, "map\\\\mp009_00.eff")
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 23)
    OP_8C(0x9, 0, 0)
    Sleep(500)
    Fade(500)
    LoadEffect(0x2, "map\\mp102_00.eff")
    OP_23(0x14A)
    OP_23(0x143)
    OP_82(0x3, 0x0)

    def lambda_C3C1():
        OP_8F(0xFE, 0xDAC, 0xBB8, 0x23F0, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_C3C1)
    OP_6D(9480, 3200, 9470, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(44000, 0)
    OP_6E(553, 0)

    def lambda_C419():
        OP_6D(10810, 3700, 8730, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C419)
    OP_72(0x1, 0x20)
    OP_70(0x1, 0x43D)
    SetChrFlags(0x9, 0x4)
    OP_82(0x0, 0x2)
    OP_22(0xA3, 0x0, 0x64)
    OP_CF(0x9, 0x1, "Frame140_on_r_arm")
    OP_8C(0x9, 180, 0)

    def lambda_C467():
        OP_96(0xFE, 0x1298, 0x1B58, 0xDFC, 0x514, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C467)

    def lambda_C485():
        OP_99(0xFE, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C485)
    Sleep(300)

    def lambda_C49A():
        OP_99(0xFE, 0x2, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C49A)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x9, 0x2)
    LoadEffect(0x7, "map\\mp101_00.eff")
    OP_8C(0x9, 180, 0)
    SetChrFlags(0x9, 0x20)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 17)
    OP_CF(0x9, 0x1, "Frame141_on_r_arm")
    ClearChrFlags(0x9, 0x4)
    OP_8C(0x9, 0, 0)
    PlayEffect(0x7, 0xFF, 0x8, 1300, 2600, -5200, 140, 0, -2, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_22(0x9B, 0x0, 0x64)
    OP_22(0x14B, 0x0, 0x64)

    def lambda_C543():
        OP_7C(0x12C, 0x12C, 0xBB8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C543)
    OP_43(0x9, 0x3, 0x0, 0x12)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    Sleep(1000)

    ChrTalk(    #344
        0x9,
        "#126F#1PHya!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(370, 70, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #345
        (
            "\x07\x05Absurd... Absurd!\x01",
            "The Aureole's barrier is absolute!\x01",
            "It cannot be harmed by...!\x02\x03",

            "Wait!\x02\x03",

            "That sword! Of course!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #346
        0x9,
        (
            "#124F#1PYes. The sword granted to me by\x01",
            "the Grandmaster.\x02\x03",

            "#123FJust like your staff. It's a demon sword\x01",
            "forged through the Divergent Laws.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(370, 70, -1, -1)
    SetChrName("Weissmann's Voice")

    AnonymousTalk(    #347
        (
            "\x07\x05Kkh... Careless of me...\x02\x03",

            "Curse you... Get away...\x02\x03",

            "Get away...you insect!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_C711():
        OP_6B(3000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C711)
    LoadEffect(0x5, "monster\\ms31002a.eff")
    OP_43(0x8, 0x0, 0x0, 0x11)
    Sleep(500)

    def lambda_C744():

        label("loc_C744")

        OP_9E(0xFE, 0x5DC, 0x5DC, 0x1F4, 0x1388)
        OP_48()
        Jump("loc_C744")

    QueueWorkItem2(0x20, 2, lambda_C744)
    Sleep(1000)
    SetChrPos(0x101, -8200, 200, -900, 90)
    SetChrPos(0x102, -8200, 200, 750, 90)
    SetChrPos(0xF8, -9600, 200, -850, 90)
    SetChrPos(0xF9, -9600, 200, 850, 90)

    ChrTalk(    #348 op#A op#5
        0x9,
        "#1432F#5P#10AGuh...\x05\x02",
    )

    Sleep(1000)
    Sleep(1000)
    OP_43(0x8, 0x0, 0x0, 0x10)
    Sleep(1000)

    ChrTalk(    #349 op#A
        0x9,
        "#1430F#5P#30AHah. Too late...\x02",
    )

    Sleep(2000)
    OP_44(0x20, 0x3)
    Sleep(500)
    OP_82(0x2, 0x2)
    PlayEffect(0x2, 0x1, 0x8, 0, 3000, 0, 150, 0, 0, 1200, 800, 1200, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 23)
    SetChrSubChip(0x9, 5)

    def lambda_C850():
        OP_99(0xFE, 0x5, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C850)
    OP_44(0x9, 0x3)
    OP_44(0x101, 0x0)
    OP_22(0x9B, 0x0, 0x64)
    OP_22(0x139, 0x0, 0x64)
    Fade(500)
    LoadEffect(0x7, "monster\\ms31002c.eff")
    OP_0D()
    OP_82(0x3, 0x2)
    OP_82(0x6, 0x2)
    OP_44(0x8, 0x0)
    OP_44(0x20, 0x2)

    def lambda_C89D():
        OP_6D(-5870, 200, 14300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C89D)

    def lambda_C8B5():
        OP_67(0, 5510, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C8B5)

    def lambda_C8CD():
        OP_6B(2200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C8CD)

    def lambda_C8DD():
        OP_6E(500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C8DD)
    OP_43(0x9, 0x0, 0x0, 0xD)
    OP_43(0x20, 0x0, 0x0, 0xE)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x20, 0x0)
    OP_73(0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #350
        0x101,
        "#1020F#1POh, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x102,
        "#1046F#1P#3SLOEWE!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)

    def lambda_C94A():
        OP_6B(1900, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C94A)
    SetChrSubChip(0x9, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #352
        0x9,
        (
            "#121F#5PForget about me!\x02\x03",

            "Your path...is clear!\x01",
            "Strike him down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x102,
        "#1043F#1PLoewe...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-5210, 200, 7340, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(45000, 0)
    OP_6E(479, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)
    SetChrPos(0x101, -8200, 200, -900, 90)
    SetChrPos(0x102, -8200, 200, 750, 90)
    SetChrPos(0xF8, -9600, 200, -850, 90)
    SetChrPos(0xF9, -9600, 200, 850, 90)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0xF8, 11)
    SetChrChipByIndex(0xF9, 13)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    OP_8C(0x101, 0, 0)
    OP_8C(0x102, 0, 0)
    OP_8C(0xF8, 0, 0)
    OP_8C(0xF9, 0, 0)
    SetChrPos(0x8, 9580, 5500, 0, 270)

    def lambda_CADA():
        OP_6D(12800, 7190, 1790, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CADA)

    def lambda_CAF2():
        OP_67(0, 2980, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CAF2)

    def lambda_CB0A():
        OP_6B(2520, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CB0A)

    def lambda_CB1A():
        OP_6C(69000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CB1A)

    def lambda_CB2A():
        OP_6E(466, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CB2A)

    def lambda_CB3A():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CB3A)
    Sleep(100)

    def lambda_CB4D():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CB4D)
    Sleep(100)

    def lambda_CB60():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_CB60)
    Sleep(100)

    def lambda_CB73():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_CB73)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    SetChrName("Weissmann's Voice")
    SetMessageWindowPos(210, 260, -1, -1)

    AnonymousTalk(    #354
        (
            "\x07\x05You dare strike one such as I...?\x02\x03",

            "No matter. The absolute barrier is\x01",
            "but a trifle of the Aureole's power.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    LoadEffect(0x0, "monster\\\\ms31000.eff")
    Sleep(500)

    def lambda_CC3A():
        OP_6B(3600, 20000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CC3A)
    OP_43(0x8, 0x1, 0x0, 0xC)
    Sleep(3500)
    SetChrName("Weissmann's Voice")
    SetMessageWindowPos(200, 260, -1, -1)

    AnonymousTalk(    #355
        (
            "\x07\x05I shall bring forth its full force and\x01",
            "let you savor the despair.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CCEB")

    ChrTalk(    #356
        0x110,
        "#271FThat is our line, monster!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEEB")

    label("loc_CCEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD2A")

    ChrTalk(    #357
        0x106,
        "#054F#5PJust try it, you son of a bitch!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEEB")

    label("loc_CD2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD65")

    ChrTalk(    #358
        0x103,
        "#024F#5PI don't think so, Weissmann!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEEB")

    label("loc_CD65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD99")

    ChrTalk(    #359
        0x108,
        "#076F#5PWe will never falter!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEEB")

    label("loc_CD99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDDF")

    ChrTalk(    #360
        0x104,
        "#530F#5PNay, fiend. The despair shall be yours!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEEB")

    label("loc_CDDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE2B")

    ChrTalk(    #361
        0x109,
        (
            "#1069F#5POh, you wanna talk DESPAIR,\x01",
            "well here we go!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEEB")

    label("loc_CE2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE70")

    ChrTalk(    #362
        0x10F,
        "#177FYour 'despair' will never stop us, beast!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEEB")

    label("loc_CE70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CEAF")

    ChrTalk(    #363
        0x10B,
        "#214F#5PNo way, monster! You're through!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEEB")

    label("loc_CEAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CEEB")

    ChrTalk(    #364
        0x105,
        "#1166F#5PNever! Our hope will never die!\x02",
    )

    CloseMessageWindow()

    label("loc_CEEB")


    ChrTalk(    #365
        0x101,
        (
            "#1022F#5POkay, you! As a bracer!\x01",
            "As a citizen of Liberl!\x02\x03",

            "#1005FAnd more than anything, as a human being!\x01",
            "I'm TAKING YOU DOWN!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x102,
        "#1046F#5PWeissmann...this is the end!\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    WaitChrThread(0x8, 0x1)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xC)
    OP_22(0x14C, 0x0, 0x64)
    Sleep(1000)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x8, 0xFF)
    OP_23(0x149)
    Battle(0x451, 0x300016, 0x0, 0x80, 0xFF)
    Return()

    # Function_10_A836 end

    def Function_11_CFDE(): pass

    label("Function_11_CFDE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_BB(0x1, 0x0, 0x200042)
    OP_BB(0x1, 0x1, 0x1C)
    OP_BD()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5318   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_11_CFDE end

    def Function_12_D006(): pass

    label("Function_12_D006")

    Fade(500)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 211)
    OP_70(0x0, 0xFA)
    OP_22(0x8F, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 251)
    OP_70(0x0, 0x122)
    Play3DEffect(0x0, 0x3, 0x0, "Frame95__ball", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_22(0xD7, 0x0, 0x64)
    Return()

    # Function_12_D006 end

    def Function_13_D073(): pass

    label("Function_13_D073")

    OP_CF(0x9, 0x1, "Frame140_on_r_arm")
    ClearChrFlags(0x9, 0x2)
    OP_8C(0x9, 180, 0)
    SetChrFlags(0x9, 0x4)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 24)
    OP_96(0x9, 0xFFFFE066, 0xC8, 0x30D4, 0xBB8, 0xBB8)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 4)
    SetChrChipByIndex(0x9, 2)
    Return()

    # Function_13_D073 end

    def Function_14_D0D0(): pass

    label("Function_14_D0D0")


    def lambda_D0D6():
        OP_8F(0xFE, 0xED8, 0xBB8, 0x1C84, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_D0D6)
    OP_72(0x1, 0x20)
    OP_D8(0x1, 0x1F4)
    OP_B0(0x1, 0x19)
    OP_6F(0x1, 1078)
    OP_70(0x1, 0x438)
    OP_73(0x1)
    OP_B0(0x1, 0x14)
    OP_6F(0x1, 1101)
    OP_70(0x1, 0x47E)
    Sleep(100)

    def lambda_D126():
        OP_96(0xFE, 0xFFFFF448, 0xC8, 0x2710, 0x1F4, 0x3A98)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_D126)
    WaitChrThread(0x20, 0x2)
    OP_22(0xF6, 0x0, 0x64)
    Return()

    # Function_14_D0D0 end

    def Function_15_D149(): pass

    label("Function_15_D149")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D18F")
    Sleep(1500)
    PlayEffect(0x4, 0xFF, 0x8, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("Function_15_D149")

    label("loc_D18F")

    Return()

    # Function_15_D149 end

    def Function_16_D190(): pass

    label("Function_16_D190")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D20B")
    PlayEffect(0x5, 0xFF, 0x8, 0, 1500, 3000, 0, 0, 0, 3000, 3000, 3000, 0x20, 0, 2500, 0, 0)
    PlayEffect(0x5, 0xFF, 0x8, 0, 1500, 3000, 0, 0, 0, 2000, 2000, 2000, 0x9, 0, 0, 0, 0)
    Sleep(2000)
    Jump("Function_16_D190")

    label("loc_D20B")

    Return()

    # Function_16_D190 end

    def Function_17_D20C(): pass

    label("Function_17_D20C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D287")
    PlayEffect(0x5, 0xFF, 0x8, 0, 1500, 3000, 0, 0, 0, 3000, 3000, 3000, 0x20, 0, 2500, 0, 0)
    PlayEffect(0x5, 0xFF, 0x8, 0, 1500, 3000, 0, 0, 0, 2000, 2000, 2000, 0x9, 0, 500, 0, 0)
    Sleep(3500)
    Jump("Function_17_D20C")

    label("loc_D287")

    Return()

    # Function_17_D20C end

    def Function_18_D288(): pass

    label("Function_18_D288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D2CE")
    PlayEffect(0x6, 0x7, 0x9, -200, 1000, 1000, 140, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jump("Function_18_D288")

    label("loc_D2CE")

    Return()

    # Function_18_D288 end

    def Function_19_D2CF(): pass

    label("Function_19_D2CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D303")
    OP_22(0xF8, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xF8, 0x0, 0x64)
    Sleep(1400)
    OP_22(0xF8, 0x0, 0x64)
    Sleep(1200)
    OP_22(0xF8, 0x0, 0x64)
    Sleep(1300)
    Jump("Function_19_D2CF")

    label("loc_D303")

    Return()

    # Function_19_D2CF end

    def Function_20_D304(): pass

    label("Function_20_D304")

    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 25)
    SetChrPos(0xFE, -2400, 6000, 4300, 270)

    def lambda_D32A():

        label("loc_D32A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D32A")

    QueueWorkItem2(0xFE, 3, lambda_D32A)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    Sleep(100)
    OP_7D(0x0, 0xFE, 0x46, 0x1F4)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 20)
    OP_90(0xFE, 0x0, 0xFFFFF704, 0xFFFFF830, 0x36B0, 0x0)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    OP_8C(0xFE, 270, 100)
    Return()

    # Function_20_D304 end

    def Function_21_D392(): pass

    label("Function_21_D392")

    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 25)
    SetChrPos(0xFE, 2000, 6500, 3200, 270)

    def lambda_D3B8():

        label("loc_D3B8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D3B8")

    QueueWorkItem2(0xFE, 3, lambda_D3B8)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    Sleep(150)
    OP_7D(0x0, 0xFE, 0x46, 0x1F4)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 20)
    OP_90(0xFE, 0xFFFFF830, 0xFFFFF8F8, 0xFFFFF830, 0x36B0, 0x0)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    OP_8C(0xFE, 270, 100)
    Return()

    # Function_21_D392 end

    def Function_22_D420(): pass

    label("Function_22_D420")

    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 25)
    SetChrPos(0xFE, -2400, 5500, -4300, 270)

    def lambda_D446():

        label("loc_D446")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D446")

    QueueWorkItem2(0xFE, 3, lambda_D446)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    Sleep(200)
    OP_7D(0x0, 0xFE, 0x46, 0x1F4)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 20)
    OP_90(0xFE, 0x0, 0xFFFFF8F8, 0x7D0, 0x36B0, 0x0)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    OP_8C(0xFE, 270, 100)
    Return()

    # Function_22_D420 end

    def Function_23_D4AE(): pass

    label("Function_23_D4AE")

    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 25)
    SetChrPos(0xFE, 1500, 6000, -2700, 270)

    def lambda_D4D4():

        label("loc_D4D4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D4D4")

    QueueWorkItem2(0xFE, 3, lambda_D4D4)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x99, 0x0, 0x64)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    Sleep(180)
    OP_7D(0x0, 0xFE, 0x46, 0x1F4)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 20)
    OP_90(0xFE, 0xFFFFFA24, 0xFFFFFAEC, 0x5DC, 0x36B0, 0x0)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    OP_8C(0xFE, 270, 100)
    Return()

    # Function_23_D4AE end

    def Function_24_D53C(): pass

    label("Function_24_D53C")

    OP_7D(0x0, 0xFE, 0x55, 0xFA0)
    OP_97(0xFE, 0xFFFFD396, 0xC8, 0xFFFD40E0, 0x2328, 0x2)
    OP_97(0xFE, 0xFFFFD396, 0xC8, 0xFFFD40E0, 0x2710, 0x2)
    OP_97(0xFE, 0xFFFFD396, 0xC8, 0xFFFD40E0, 0x2EE0, 0x2)

    label("loc_D583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D5AA")
    OP_7D(0x0, 0xFE, 0x55, 0xCE4)
    OP_97(0xFE, 0xFFFFD396, 0xC8, 0xFFFA81C0, 0x36B0, 0x2)
    Jump("loc_D583")

    label("loc_D5AA")

    OP_7D(0x1, 0xFE, 0x0, 0x0)
    OP_97(0xFE, 0xFFFFD396, 0xC8, 0xFFFD40E0, 0x2EE0, 0x2)
    OP_A2(0x1)
    Return()

    # Function_24_D53C end

    def Function_25_D5CB(): pass

    label("Function_25_D5CB")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 10)
    SetChrPos(0xFE, -7890, 200, 290, 270)
    SetChrSubChip(0xFE, 6)
    PlayEffect(0x1, 0xFF, 0x101, -200, 400, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D640():
        OP_8F(0xFE, 0xFFFFD396, 0xC8, 0xC8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D640)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_D5CB end

    def Function_26_D660(): pass

    label("Function_26_D660")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 10)
    SetChrPos(0xFE, -16270, 200, 50, 90)
    SetChrSubChip(0xFE, 6)
    PlayEffect(0x1, 0xFF, 0x101, 300, 300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D6D5():
        OP_8F(0xFE, 0xFFFFD396, 0xC8, 0xC8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D6D5)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_D660 end

    def Function_27_D6F5(): pass

    label("Function_27_D6F5")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 10)
    SetChrPos(0xFE, -9630, 200, -3370, 315)
    SetChrSubChip(0xFE, 6)
    PlayEffect(0x1, 0xFF, 0x101, 100, 0, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D76A():
        OP_8F(0xFE, 0xFFFFD396, 0xC8, 0xC8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D76A)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_D6F5 end

    def Function_28_D78A(): pass

    label("Function_28_D78A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 10)
    SetChrPos(0xFE, -14920, 200, 3400, 135)
    SetChrSubChip(0xFE, 6)
    PlayEffect(0x1, 0xFF, 0x101, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D7FF():
        OP_8F(0xFE, 0xFFFFD396, 0xC8, 0xC8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7FF)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_D78A end

    def Function_29_D81F(): pass

    label("Function_29_D81F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 10)
    SetChrPos(0xFE, -9510, 200, 3440, 225)
    SetChrSubChip(0xFE, 6)
    PlayEffect(0x1, 0xFF, 0x101, 200, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D894():
        OP_8F(0xFE, 0xFFFFD396, 0xC8, 0xC8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D894)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_D81F end

    def Function_30_D8B4(): pass

    label("Function_30_D8B4")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 10)
    SetChrPos(0xFE, -14510, 200, -3560, 45)
    SetChrSubChip(0xFE, 6)
    PlayEffect(0x1, 0xFF, 0x101, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D929():
        OP_8F(0xFE, 0xFFFFD396, 0xC8, 0xC8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D929)

    def lambda_D944():
        TurnDirection(0xFE, 0x1D, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D944)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_D8B4 end

    def Function_31_D957(): pass

    label("Function_31_D957")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D9A3")
    OP_51(0x9, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1D, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1D, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1D, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1D, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1D, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1D, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_31_D957")

    label("loc_D9A3")

    Return()

    # Function_31_D957 end

    def Function_32_D9A4(): pass

    label("Function_32_D9A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D9E8")
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_83(0x0, 0x2)
    Jump("Function_32_D9A4")

    label("loc_D9E8")

    Return()

    # Function_32_D9A4 end

    def Function_33_D9E9(): pass

    label("Function_33_D9E9")

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
        (0, "loc_DA62"),
        (1, "loc_DA68"),
        (SWITCH_DEFAULT, "loc_DA6E"),
    )


    label("loc_DA62")

    OP_A2(0x1200)
    Jump("loc_DA6E")

    label("loc_DA68")

    OP_A2(0x1201)
    Jump("loc_DA6E")

    label("loc_DA6E")

    Return()

    # Function_33_D9E9 end

    def Function_34_DA6F(): pass

    label("Function_34_DA6F")

    FadeToDark(0, 0, -1)
    OP_6D(-211220, -20490, -48190, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xE, 0xF, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_34_DA6F end

    SaveToFile()

Try(main)
