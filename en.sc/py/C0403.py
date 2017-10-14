from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0403   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 16,
        MapDefaultBGM       = "ed60033",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C0403_1 ._SN',
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
        'Crow',                                 # 9
        '',                                     # 10
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT06/CH20100 ._CH',             # 02
        'ED6_DT07/CH02100 ._CH',             # 03
        'ED6_DT27/CH03520 ._CH',             # 04
        'ED6_DT27/CH03500 ._CH',             # 05
        'ED6_DT27/CH03600 ._CH',             # 06
        'ED6_DT27/CH03530 ._CH',             # 07
        'ED6_DT26/CH20280 ._CH',             # 08
        'ED6_DT27/CH03500 ._CH',             # 09
        'ED6_DT06/CH20021 ._CH',             # 0A
        'ED6_DT27/CH03870 ._CH',             # 0B
        'ED6_DT27/CH03871 ._CH',             # 0C
        'ED6_DT27/CH03005 ._CH',             # 0D
        'ED6_DT29/CH12140 ._CH',             # 0E
        'ED6_DT29/CH12141 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT06/CH20100P._CP',             # 02
        'ED6_DT07/CH02100P._CP',             # 03
        'ED6_DT27/CH03520P._CP',             # 04
        'ED6_DT27/CH03500P._CP',             # 05
        'ED6_DT27/CH03600P._CP',             # 06
        'ED6_DT27/CH03530P._CP',             # 07
        'ED6_DT26/CH20280P._CP',             # 08
        'ED6_DT27/CH03500P._CP',             # 09
        'ED6_DT06/CH20021P._CP',             # 0A
        'ED6_DT27/CH03870P._CP',             # 0B
        'ED6_DT27/CH03871P._CP',             # 0C
        'ED6_DT27/CH03005P._CP',             # 0D
        'ED6_DT29/CH12140P._CP',             # 0E
        'ED6_DT29/CH12141P._CP',             # 0F
    )

    DeclNpc(
        X                   = -5140,
        Z                   = 250,
        Y                   = 1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -9470,
        Z                   = 250,
        Y                   = 3200,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x31,
        Unknown_18          = 8449,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -5140,
        TriggerZ            = 250,
        TriggerY            = 1000,
        TriggerRange        = 1000,
        ActorX              = -5140,
        ActorZ              = 250,
        ActorY              = 1000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_1CD",          # 01, 1
        "Function_2_269",          # 02, 2
        "Function_3_493",          # 03, 3
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 1)), scpexpr(EXPR_END)), "loc_196")
    SetChrFlags(0x9, 0x80)

    label("loc_196")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC")
    OP_B5(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_1BC")

    label("loc_1B8")

    OP_44(0x8, 0x0)

    label("loc_1BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CC")
    OP_44(0x8, 0x0)

    label("loc_1CC")

    Return()

    # Function_0_18A end

    def Function_1_1CD(): pass

    label("Function_1_1CD")

    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_247")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247")
    OP_65(0x0, 0x1)
    SoundLoad(347)
    SoundLoad(140)
    LoadEffect(0x0, "map\\\\mp022_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -5140, 450, 1000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_247")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_259")
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)

    label("loc_259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_263")
    OP_82(0x80, 0x0)

    label("loc_263")

    OP_22(0x1C3, 0x1, 0x64)
    Return()

    # Function_1_1CD end

    def Function_2_269(): pass

    label("Function_2_269")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -5140, -470, -7400, 2650, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_492")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45B")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_324")

    def lambda_308():

        label("loc_308")

        OP_97(0xFE, 0xFFFFF060, 0x3E8, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_308")

    QueueWorkItem2(0xFE, 1, lambda_308)
    Jump("loc_343")

    label("loc_324")


    def lambda_32A():

        label("loc_32A")

        OP_97(0xFE, 0xFFFFF060, 0x3E8, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_32A")

    QueueWorkItem2(0xFE, 1, lambda_32A)

    label("loc_343")

    SetChrChipByIndex(0xFE, 11)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    OP_22(0x15B, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)

    label("loc_35C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_394")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38C")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_394")

    label("loc_38C")

    Sleep(15)
    Jump("loc_35C")

    label("loc_394")

    OP_44(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -5140, 251, 1000, 270)

    label("loc_3B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_458")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3A98), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3A98), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3A98), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3A98), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_450")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_450")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 12)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -5140, 250, 1000, 270)
    OP_8D(0xFE, -5140, -470, -7400, 2650, 0)
    Jump("loc_458")

    label("loc_450")

    Sleep(500)
    Jump("loc_3B3")

    label("loc_458")

    Jump("loc_48F")

    label("loc_45B")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F")

    def lambda_477():
        OP_8D(0xFE, -5140, -470, -7400, 2650, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_477)

    label("loc_48F")

    Jump("loc_29D")

    label("loc_492")

    Return()

    # Function_2_269 end

    def Function_3_493(): pass

    label("Function_3_493")

    Call(1, 0)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_3_493 end

    SaveToFile()

Try(main)
