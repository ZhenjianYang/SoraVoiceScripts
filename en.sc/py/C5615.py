from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5615   ._SN',
        MapName             = 'Other',
        Location            = 'C5615.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60061",
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
        'Anelace',                              # 9
        'Vogel 235',                            # 10
        'Vogel 235',                            # 11
        'Vogel 570',                            # 12
        'Vogel 570',                            # 13
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
        'ED6_DT07/CH01630 ._CH',             # 00
        'ED6_DT27/CH04000 ._CH',             # 01
        'ED6_DT27/CH04001 ._CH',             # 02
        'ED6_DT07/CH00120 ._CH',             # 03
        'ED6_DT07/CH00121 ._CH',             # 04
        'ED6_DT07/CH00150 ._CH',             # 05
        'ED6_DT07/CH00151 ._CH',             # 06
        'ED6_DT07/CH00130 ._CH',             # 07
        'ED6_DT07/CH00131 ._CH',             # 08
        'ED6_DT07/CH00140 ._CH',             # 09
        'ED6_DT07/CH00141 ._CH',             # 0A
        'ED6_DT07/CH00160 ._CH',             # 0B
        'ED6_DT07/CH00161 ._CH',             # 0C
        'ED6_DT07/CH00170 ._CH',             # 0D
        'ED6_DT07/CH00171 ._CH',             # 0E
        'ED6_DT27/CH04080 ._CH',             # 0F
        'ED6_DT27/CH04081 ._CH',             # 10
        'ED6_DT07/CH00421 ._CH',             # 11
        'ED6_DT29/CH12330 ._CH',             # 12
        'ED6_DT26/CH20406 ._CH',             # 13
        'ED6_DT07/CH00420 ._CH',             # 14
        'ED6_DT27/CH03084 ._CH',             # 15
        'ED6_DT26/CH20373 ._CH',             # 16
        'ED6_DT29/CH12570 ._CH',             # 17
        'ED6_DT29/CH12571 ._CH',             # 18
        'ED6_DT29/CH12350 ._CH',             # 19
        'ED6_DT29/CH12351 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH01630P._CP',             # 00
        'ED6_DT27/CH04000P._CP',             # 01
        'ED6_DT27/CH04001P._CP',             # 02
        'ED6_DT07/CH00120P._CP',             # 03
        'ED6_DT07/CH00121P._CP',             # 04
        'ED6_DT07/CH00150P._CP',             # 05
        'ED6_DT07/CH00151P._CP',             # 06
        'ED6_DT07/CH00130P._CP',             # 07
        'ED6_DT07/CH00131P._CP',             # 08
        'ED6_DT07/CH00140P._CP',             # 09
        'ED6_DT07/CH00141P._CP',             # 0A
        'ED6_DT07/CH00160P._CP',             # 0B
        'ED6_DT07/CH00161P._CP',             # 0C
        'ED6_DT07/CH00170P._CP',             # 0D
        'ED6_DT07/CH00171P._CP',             # 0E
        'ED6_DT27/CH04080P._CP',             # 0F
        'ED6_DT27/CH04081P._CP',             # 10
        'ED6_DT07/CH00421P._CP',             # 11
        'ED6_DT29/CH12330P._CP',             # 12
        'ED6_DT26/CH20406P._CP',             # 13
        'ED6_DT07/CH00420P._CP',             # 14
        'ED6_DT27/CH03084P._CP',             # 15
        'ED6_DT26/CH20373P._CP',             # 16
        'ED6_DT29/CH12570P._CP',             # 17
        'ED6_DT29/CH12571P._CP',             # 18
        'ED6_DT29/CH12350P._CP',             # 19
        'ED6_DT29/CH12351P._CP',             # 1A
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -157870,
        TriggerZ            = 0,
        TriggerY            = 100,
        TriggerRange        = 800,
        ActorX              = -157870,
        ActorZ              = 1000,
        ActorY              = 100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_246",          # 00, 0
        "Function_1_25F",          # 01, 1
        "Function_2_269",          # 02, 2
        "Function_3_27F",          # 03, 3
        "Function_4_62D",          # 04, 4
        "Function_5_68B",          # 05, 5
        "Function_6_6E9",          # 06, 6
        "Function_7_747",          # 07, 7
        "Function_8_7A5",          # 08, 8
        "Function_9_8DC",          # 09, 9
        "Function_10_987",         # 0A, 10
        "Function_11_1D1B",        # 0B, 11
        "Function_12_1F5A",        # 0C, 12
        "Function_13_1FE3",        # 0D, 13
    )


    def Function_0_246(): pass

    label("Function_0_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E")
    Event(0, 3)

    label("loc_25E")

    Return()

    # Function_0_246 end

    def Function_1_25F(): pass

    label("Function_1_25F")

    OP_74(0x0, 0x0, 0x0)
    Return()

    # Function_1_25F end

    def Function_2_269(): pass

    label("Function_2_269")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_269")

    label("loc_27E")

    Return()

    # Function_2_269 end

    def Function_3_27F(): pass

    label("Function_3_27F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_296")
    Call(0, 12)
    Call(0, 13)

    label("loc_296")

    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, -153870, 0, -30, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x109, -143220, 10, 460, 270)
    SetChrPos(0x101, -143310, 10, -640, 270)
    SetChrPos(0xF8, -142050, 0, 460, 270)
    SetChrPos(0xF9, -142050, 0, -640, 270)
    OP_6D(-142530, 0, 0, 0)
    OP_67(0, 7700, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(315000, 0)
    OP_6E(265, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1002F#6P...!\x02",
    )

    CloseMessageWindow()

    def lambda_35F():
        OP_6D(-151430, 0, 550, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35F)

    def lambda_377():
        OP_67(0, 5420, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_377)

    def lambda_38F():
        OP_6B(1950, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38F)

    def lambda_39F():
        OP_6E(404, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_39F)
    Sleep(2000)
    OP_8C(0x8, 90, 400)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    Sleep(1000)

    ChrTalk(    #1
        0x8,
        "#1313F#6P...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x109, 15)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_410"),
        (5, "loc_418"),
        (3, "loc_420"),
        (4, "loc_428"),
        (6, "loc_430"),
        (7, "loc_438"),
        (SWITCH_DEFAULT, "loc_440"),
    )


    label("loc_410")

    SetChrChipByIndex(0xF8, 3)
    Jump("loc_440")

    label("loc_418")

    SetChrChipByIndex(0xF8, 5)
    Jump("loc_440")

    label("loc_420")

    SetChrChipByIndex(0xF8, 7)
    Jump("loc_440")

    label("loc_428")

    SetChrChipByIndex(0xF8, 9)
    Jump("loc_440")

    label("loc_430")

    SetChrChipByIndex(0xF8, 11)
    Jump("loc_440")

    label("loc_438")

    SetChrChipByIndex(0xF8, 13)
    Jump("loc_440")

    label("loc_440")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_461"),
        (5, "loc_469"),
        (3, "loc_471"),
        (4, "loc_479"),
        (6, "loc_481"),
        (7, "loc_489"),
        (SWITCH_DEFAULT, "loc_491"),
    )


    label("loc_461")

    SetChrChipByIndex(0xF9, 3)
    Jump("loc_491")

    label("loc_469")

    SetChrChipByIndex(0xF9, 5)
    Jump("loc_491")

    label("loc_471")

    SetChrChipByIndex(0xF9, 7)
    Jump("loc_491")

    label("loc_479")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_491")

    label("loc_481")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_491")

    label("loc_489")

    SetChrChipByIndex(0xF9, 13)
    Jump("loc_491")

    label("loc_491")


    def lambda_497():
        OP_91(0xFE, 0xFFFFEF34, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_497)
    Sleep(60)

    def lambda_4B7():
        OP_91(0xFE, 0xFFFFEF34, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4B7)
    Sleep(100)

    def lambda_4D7():
        OP_91(0xFE, 0xFFFFEF98, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4D7)
    Sleep(70)

    def lambda_4F7():
        OP_91(0xFE, 0xFFFFEF98, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4F7)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #2
        0x101,
        "#1002F#2PSo they got Anelace too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        "#1069F#2PWe need to pin her down for a minute!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_43(0x9, 0x0, 0x0, 0x4)
    Sleep(200)
    OP_43(0xA, 0x0, 0x0, 0x5)
    Sleep(200)
    OP_43(0xB, 0x0, 0x0, 0x6)
    Sleep(200)
    OP_43(0xC, 0x0, 0x0, 0x7)
    Sleep(1500)

    def lambda_5A9():
        OP_6D(-151500, 0, 500, 300)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5A9)

    def lambda_5C1():
        OP_6B(1760, 300)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5C1)
    OP_43(0x101, 0x0, 0x0, 0x8)
    OP_43(0x8, 0x0, 0x0, 0x9)
    Sleep(300)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x420, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_623"),
        (SWITCH_DEFAULT, "loc_628"),
    )


    label("loc_623")

    OP_B4(0x0)
    Jump("loc_628")

    label("loc_628")

    Call(0, 10)
    Return()

    # Function_3_27F end

    def Function_4_62D(): pass

    label("Function_4_62D")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -154580, 1200, 1920, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_66A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_66A)
    OP_8F(0xFE, 0xFFFDA42C, 0x0, 0x780, 0x7D0, 0x0)
    Return()

    # Function_4_62D end

    def Function_5_68B(): pass

    label("Function_5_68B")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -154600, 1200, -1460, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_6C8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6C8)
    OP_8F(0xFE, 0xFFFDA418, 0x0, 0xFFFFFA4C, 0x7D0, 0x0)
    Return()

    # Function_5_68B end

    def Function_6_6E9(): pass

    label("Function_6_6E9")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -156040, 1200, 1040, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_726():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_726)
    OP_8F(0xFE, 0xFFFD9E78, 0x0, 0x410, 0x7D0, 0x0)
    Return()

    # Function_6_6E9 end

    def Function_7_747(): pass

    label("Function_7_747")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -156170, 1210, -750, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_784():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_784)
    OP_8F(0xFE, 0xFFFD9DF6, 0x0, 0xFFFFFD12, 0x7D0, 0x0)
    Return()

    # Function_7_747 end

    def Function_8_7A5(): pass

    label("Function_8_7A5")

    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x109, 16)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_7D0"),
        (5, "loc_7D8"),
        (3, "loc_7E0"),
        (4, "loc_7E8"),
        (6, "loc_7F0"),
        (7, "loc_7F8"),
        (SWITCH_DEFAULT, "loc_800"),
    )


    label("loc_7D0")

    SetChrChipByIndex(0xF8, 4)
    Jump("loc_800")

    label("loc_7D8")

    SetChrChipByIndex(0xF8, 6)
    Jump("loc_800")

    label("loc_7E0")

    SetChrChipByIndex(0xF8, 8)
    Jump("loc_800")

    label("loc_7E8")

    SetChrChipByIndex(0xF8, 10)
    Jump("loc_800")

    label("loc_7F0")

    SetChrChipByIndex(0xF8, 12)
    Jump("loc_800")

    label("loc_7F8")

    SetChrChipByIndex(0xF8, 14)
    Jump("loc_800")

    label("loc_800")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_821"),
        (5, "loc_829"),
        (3, "loc_831"),
        (4, "loc_839"),
        (6, "loc_841"),
        (7, "loc_849"),
        (SWITCH_DEFAULT, "loc_851"),
    )


    label("loc_821")

    SetChrChipByIndex(0xF9, 4)
    Jump("loc_851")

    label("loc_829")

    SetChrChipByIndex(0xF9, 6)
    Jump("loc_851")

    label("loc_831")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_851")

    label("loc_839")

    SetChrChipByIndex(0xF9, 10)
    Jump("loc_851")

    label("loc_841")

    SetChrChipByIndex(0xF9, 12)
    Jump("loc_851")

    label("loc_849")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_851")

    label("loc_851")

    SetChrFlags(0xF8, 0x1000)
    SetChrFlags(0xF9, 0x1000)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x109, 0x1000)

    def lambda_86B():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86B)
    Sleep(50)

    def lambda_88B():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_88B)

    def lambda_8A6():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8A6)
    Sleep(50)

    def lambda_8C6():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8C6)
    Return()

    # Function_8_7A5 end

    def Function_9_8DC(): pass

    label("Function_9_8DC")

    SetChrChipByIndex(0x8, 17)

    def lambda_8E7():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_8E7)
    SetChrChipByIndex(0x9, 24)

    def lambda_907():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_907)
    Sleep(50)
    SetChrChipByIndex(0xA, 24)

    def lambda_92C():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_92C)
    SetChrChipByIndex(0xB, 26)

    def lambda_94C():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_94C)
    Sleep(50)
    SetChrChipByIndex(0xC, 26)

    def lambda_971():
        OP_91(0xFE, 0xDAC, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_971)
    Return()

    # Function_9_8DC end

    def Function_10_987(): pass

    label("Function_10_987")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_44(0x8, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x8, 0x2)
    OP_44(0x8, 0x3)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x109, 15)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x8, -153000, 0, -70, 90)
    SetChrChipByIndex(0x8, 19)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x109, -150930, 20, 460, 270)
    SetChrPos(0x101, -150850, 20, -840, 270)
    SetChrPos(0xF8, -149630, 20, 460, 270)
    SetChrPos(0xF9, -149540, 20, -840, 270)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x109, 0x1000)
    ClearChrFlags(0xF8, 0x1000)
    ClearChrFlags(0xF9, 0x1000)
    OP_6D(-152380, 20, 1000, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(1920, 0)
    OP_6C(315000, 0)
    OP_6E(393, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x101,
        (
            "#1007F#5POof... Anelace...\x02\x03",

            "#1019FWhen in the heck did that little\x01",
            "goof get so strong, anyway?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB3")

    ChrTalk(    #5
        0x103,
        (
            "#524F#2PShe did spend a month training\x01",
            "with you and learning your techniques,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1025F#5POh... Good point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D39")

    label("loc_BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C25")

    ChrTalk(    #7
        0x106,
        (
            "#051F#2PShe did kinda train to not lose\x01",
            "to you, y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1025F#5POh... Good point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D39")

    label("loc_C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBA")

    ChrTalk(    #9
        0x103,
        (
            "#524F#2PAs I recall, she did spend a month\x01",
            "training with you and learning your\x01",
            "techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1025F#5POh... Good point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D39")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D39")

    ChrTalk(    #11
        0x106,
        (
            "#051F#2PUnless I'm off, she did kinda train to\x01",
            "not lose to you, y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1025F#5POh... Good point.\x02",
    )

    CloseMessageWindow()

    label("loc_D39")


    ChrTalk(    #13
        0x109,
        "#1060F#6PAll right, let's wake her up.\x02",
    )

    CloseMessageWindow()

    def lambda_D6B():
        OP_6D(-153380, 20, 1000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D6B)
    OP_8F(0x109, 0xFFFDAF08, 0x0, 0xFFFFFFE2, 0x5DC, 0x0)
    OP_8C(0x109, 270, 400)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    SetChrChipByIndex(0x109, 22)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    Sleep(1000)
    LoadEffect(0x0, "scraft\\\\sc008_02.eff")
    PlayEffect(0x0, 0xFF, 0x109, 0, 1100, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    LoadEffect(0x0, "scraft\\\\sc001_05.eff")
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_9E(0x8, 0x14, 0x0, 0x1F4, 0xBB8)
    Sleep(1000)

    ChrTalk(    #14
        0x8,
        "#1312F#5PUhn...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_99(0x8, 0x0, 0x3, 0x5DC)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F2B")

    ChrTalk(    #15
        0x8,
        (
            "#1314F#5PHeehee... Estelle...everyone...\x02\x03",

            "Even Kevin's here, too...\x02\x03",

            "Thank you for coming to save me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F98")

    label("loc_F2B")


    ChrTalk(    #16
        0x8,
        (
            "#1314F#5PHeehee... Estelle...everyone...\x02\x03",

            "Even Kevin's here, too...\x02\x03",

            "Thank you for coming to save me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F98")

    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    OP_0D()

    def lambda_FAE():
        OP_8F(0x109, 0xFFFDB26E, 0x14, 0x1CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FAE)

    ChrTalk(    #17
        0x101,
        "#1025F#2PAnelace, you feel okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#1311F#5PY-Yeah... Nothing a soak at Elmo can't fix.\x02\x03",

            "#812FMore importantly...the others?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A5")

    ChrTalk(    #19
        0x103,
        (
            "#021F#2PDon't worry, we freed them all.\x02\x03",

            "You're the last one, in fact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_10A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FD")

    ChrTalk(    #20
        0x106,
        (
            "#051F#2PDon't sweat it, we freed 'em all.\x02\x03",

            "You were the last one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_10FD")


    ChrTalk(    #21
        0x109,
        (
            "#1062F#2PIt's okay, they've all been freed.\x02\x03",

            "#1061FYou're the last one we found!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1153")


    ChrTalk(    #22
        0x8,
        (
            "#1314F#5POh, I see... That's good...\x02\x03",

            "#1316FSorry, Estelle...\x02\x03",

            "I promised we'd have a big rival fight,\x01",
            "but I didn't want it to be like this...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E2")

    ChrTalk(    #23
        0x101,
        (
            "#1006F#2PDon't worry, you silly.\x02\x03",

            "It's thanks to your team that we knew\x01",
            "about this place at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x103,
        "#021F#2PYou did your job just fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x106,
        "#051F#2PYou just leave the rest to us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "#1314F#5PEstelle...everyone...\x02",
    )

    CloseMessageWindow()
    Jump("loc_158D")

    label("loc_12E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C8")

    ChrTalk(    #27
        0x101,
        (
            "#1006F#2PDon't worry, you silly.\x02\x03",

            "It's thanks to your team that we knew\x01",
            "about this place at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#021F#2PYou did your job just fine.\x02\x03",

            "#020FYou can leave the rest to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        "#1314F#5PEstelle...Schera...\x02",
    )

    CloseMessageWindow()
    Jump("loc_158D")

    label("loc_13C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14DB")

    ChrTalk(    #30
        0x101,
        (
            "#1006F#2PDon't worry, you silly.\x02\x03",

            "It's thanks to your team that we knew\x01",
            "about this place at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x106,
        (
            "#051F#2PLike Estelle said. You guys did the work\x01",
            "of five bracers--each--on this one.\x02\x03",

            "You just leave the rest to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        "#1314F#5PEstelle... Agate...\x02",
    )

    CloseMessageWindow()
    Jump("loc_158D")

    label("loc_14DB")


    ChrTalk(    #33
        0x101,
        (
            "#1006F#2PDon't worry, you silly.\x02\x03",

            "It's thanks to your team that we knew\x01",
            "about this place at all!\x02\x03",

            "You guys did a great job scouting out\x01",
            "their base.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "#1314F#5PEstelle...\x02",
    )

    CloseMessageWindow()

    label("loc_158D")

    OP_62(0x8, 0x12C, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #35
        0x8,
        (
            "#1317F#5POh, scouting job! Right!\x02\x03",

            "Estelle, I... There's something\x01",
            "I've gotta tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1004F#2PHuh? What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#1317F#5PUm, well, um...\x02\x03",

            "While we were running around, I...\x01",
            "I spotted Joshua!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #38
        0x101,
        "#1020F#2P#5SWHAT?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E6")

    ChrTalk(    #39
        0x103,
        "#023F#2PYou're kidding!\x02",
    )

    CloseMessageWindow()

    label("loc_16E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_170B")

    ChrTalk(    #40
        0x106,
        "#052F#2PNo shit?!\x02",
    )

    CloseMessageWindow()

    label("loc_170B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_172D")

    ChrTalk(    #41
        0x105,
        "#043F#2PAh...!\x02",
    )

    CloseMessageWindow()

    label("loc_172D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_175A")

    ChrTalk(    #42
        0x107,
        "#065F#2PJ-Joshua's here?!\x02",
    )

    CloseMessageWindow()

    label("loc_175A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_177C")

    ChrTalk(    #43
        0x108,
        "#073F#2POh...!\x02",
    )

    CloseMessageWindow()

    label("loc_177C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_179F")

    ChrTalk(    #44
        0x104,
        "#032F#2PHmmm...\x02",
    )

    CloseMessageWindow()

    label("loc_179F")


    ChrTalk(    #45
        0x8,
        (
            "#813F#5PWhen the jaegers were chasing us down,\x01",
            "he showed up and broke through their lines.\x02\x03",

            "I recognized his clothes and black hair.\x01",
            "I'm...pretty sure it was him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1026F#2PJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        "#1317F#5PEstelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1016F#2POh! Uh, sorry.\x02\x03",

            "#1005FSo, Anelace, don't leave it THERE!\x01",
            "Where'd Joshua go?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#813F#5PI'm not sure...\x02\x03",

            "We managed to get out of that spot,\x01",
            "but ultimately they caught us.\x02\x03",

            "#812FHe could have headed for the roof,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1020F#2PThe roof?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#812F#5PThere's some kind of airship dock on the\x01",
            "roof of this building.\x02\x03",

            "I remember the soldiers and researchers\x01",
            "heading that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1002F#2POkay, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        (
            "#1063F#2PAnelace. You think you can get out\x01",
            "on your own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        "#816F#5PYeah... I'll be okay.\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0x14, 0x0, 0x12C, 0xBB8)
    OP_99(0x8, 0x3, 0x0, 0x3E8)
    Fade(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #55
        0x8,
        (
            "#817F#3PThis place is like a...a horror show.\x01",
            "There might still be something in here...\x02\x03",

            "#812FEveryone...be careful!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B31():

        label("loc_1B31")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1B31")

    QueueWorkItem2(0x101, 1, lambda_1B31)

    def lambda_1B42():

        label("loc_1B42")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1B42")

    QueueWorkItem2(0x109, 1, lambda_1B42)

    def lambda_1B53():

        label("loc_1B53")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1B53")

    QueueWorkItem2(0xF8, 1, lambda_1B53)

    def lambda_1B64():

        label("loc_1B64")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1B64")

    QueueWorkItem2(0xF9, 1, lambda_1B64)

    def lambda_1B75():
        OP_6D(-144770, 0, -460, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B75)
    OP_8E(0x8, 0xFFFDB20A, 0x14, 0xFFFFF5EC, 0x7D0, 0x0)

    def lambda_1BA1():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BA1)
    OP_8E(0x8, 0xFFFDC074, 0x14, 0xFFFFF4F2, 0x9C4, 0x0)

    def lambda_1BCF():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BCF)
    OP_8E(0x8, 0xFFFDCE98, 0xA, 0xFFFFFE02, 0x7D0, 0x0)

    def lambda_1BFD():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BFD)
    OP_8E(0x8, 0xFFFDDB4A, 0xA, 0xFFFFFF60, 0x9C4, 0x0)

    def lambda_1C2B():
        OP_8E(0xFE, 0xFFFDE0C2, 0xA, 0xFFFFFF60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C2B)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)

    def lambda_1C70():
        OP_6D(-150730, 20, 50, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C70)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #56
        0x101,
        "#1026F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x109,
        (
            "#1065F#6PNever thought Joshua would be here too...\x02\x03",

            "#1063FLet's get to the roof!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1002F#6PYeah!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C0D)
    OP_28(0x98, 0x1, 0x100)
    OP_28(0x98, 0x1, 0x200)
    OP_28(0x98, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_10_987 end

    def Function_11_1D1B(): pass

    label("Function_11_1D1B")

    EventBegin(0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x0, 0x0, 0x3)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #59
        (
            "\x07\x02#1S[About (Beta)] Based on the data collected from the\x01",
            "experiments performed throughout Liberl, the beta has\x01",
            "entered the final tuning phase.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_74(0x0, 0x0, 0x1)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #60
        (
            "\x07\x02#1SThis emulator fully simulates the functionality of the\x01",
            "original and manages a 90% synchronization rate with orbal\x01",
            "fields. As a result, its size has increased, but execution\x01",
            "of the Gospel Plan should be... (※FOLLOWING TEXT REDACTED)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3B")
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #61
        "\x07\x00Received #1020i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FC, 1)
    Sleep(500)

    label("loc_1F3B")

    OP_A2(0x1C0E)
    OP_28(0x98, 0x1, 0x800)
    OP_74(0x0, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x1)
    Return()

    # Function_11_1D1B end

    def Function_12_1F5A(): pass

    label("Function_12_1F5A")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_1FD6"),
        (1, "loc_1FDC"),
        (SWITCH_DEFAULT, "loc_1FE2"),
    )


    label("loc_1FD6")

    OP_A2(0x1200)
    Jump("loc_1FE2")

    label("loc_1FDC")

    OP_A2(0x1201)
    Jump("loc_1FE2")

    label("loc_1FE2")

    Return()

    # Function_12_1F5A end

    def Function_13_1FE3(): pass

    label("Function_13_1FE3")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_13_1FE3 end

    SaveToFile()

Try(main)
