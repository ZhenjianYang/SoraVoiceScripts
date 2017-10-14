from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5206   ._SN',
        MapName             = 'Other',
        Location            = 'C5206.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60035",
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
        '地震制御用ダミーキャラ',               # 9
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
    )

    AddCharChipPat(
        'ED6_DT29/CH12950P._CP',             # 00
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
        "Function_0_D2",           # 00, 0
        "Function_1_D3",           # 01, 1
        "Function_2_FA",           # 02, 2
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Return()

    # Function_0_D2 end

    def Function_1_D3(): pass

    label("Function_1_D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_F9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x42), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x8, 0x3, 0x0, 0x2)
    OP_22(0x85, 0x1, 0x46)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)

    label("loc_F9")

    Return()

    # Function_1_D3 end

    def Function_2_FA(): pass

    label("Function_2_FA")

    OP_C4(0x0, 0x20)

    label("loc_100")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_122")
    OP_7C(0x3C, 0x3C, 0x3E8, 0x384)
    Sleep(1000)
    Jump("loc_100")

    label("loc_122")

    Return()

    # Function_2_FA end

    SaveToFile()

Try(main)
