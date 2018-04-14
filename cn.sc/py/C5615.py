from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '亚妮拉丝',                             # 9
        '哨兵235',                              # 10
        '哨兵235',                              # 11
        '哨兵570',                              # 12
        '哨兵570',                              # 13
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
        "Function_4_632",          # 04, 4
        "Function_5_690",          # 05, 5
        "Function_6_6EE",          # 06, 6
        "Function_7_74C",          # 07, 7
        "Function_8_7AA",          # 08, 8
        "Function_9_8E1",          # 09, 9
        "Function_10_98C",         # 0A, 10
        "Function_11_1A8D",        # 0B, 11
        "Function_12_1C2A",        # 0C, 12
        "Function_13_1CB4",        # 0D, 13
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
        "#1002F#6P……！\x02",
    )

    CloseMessageWindow()

    def lambda_361():
        OP_6D(-151430, 0, 550, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_361)

    def lambda_379():
        OP_67(0, 5420, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_379)

    def lambda_391():
        OP_6B(1950, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_391)

    def lambda_3A1():
        OP_6E(404, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3A1)
    Sleep(2000)
    OP_8C(0x8, 90, 400)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    Sleep(1000)

    ChrTalk(    #1
        0x8,
        "#1313F#5P………………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x109, 15)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_427"),
        (5, "loc_42F"),
        (3, "loc_437"),
        (4, "loc_43F"),
        (6, "loc_447"),
        (7, "loc_44F"),
        (SWITCH_DEFAULT, "loc_457"),
    )


    label("loc_427")

    SetChrChipByIndex(0xF8, 3)
    Jump("loc_457")

    label("loc_42F")

    SetChrChipByIndex(0xF8, 5)
    Jump("loc_457")

    label("loc_437")

    SetChrChipByIndex(0xF8, 7)
    Jump("loc_457")

    label("loc_43F")

    SetChrChipByIndex(0xF8, 9)
    Jump("loc_457")

    label("loc_447")

    SetChrChipByIndex(0xF8, 11)
    Jump("loc_457")

    label("loc_44F")

    SetChrChipByIndex(0xF8, 13)
    Jump("loc_457")

    label("loc_457")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_478"),
        (5, "loc_480"),
        (3, "loc_488"),
        (4, "loc_490"),
        (6, "loc_498"),
        (7, "loc_4A0"),
        (SWITCH_DEFAULT, "loc_4A8"),
    )


    label("loc_478")

    SetChrChipByIndex(0xF9, 3)
    Jump("loc_4A8")

    label("loc_480")

    SetChrChipByIndex(0xF9, 5)
    Jump("loc_4A8")

    label("loc_488")

    SetChrChipByIndex(0xF9, 7)
    Jump("loc_4A8")

    label("loc_490")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_4A8")

    label("loc_498")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_4A8")

    label("loc_4A0")

    SetChrChipByIndex(0xF9, 13)
    Jump("loc_4A8")

    label("loc_4A8")


    def lambda_4AE():
        OP_91(0xFE, 0xFFFFEF34, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AE)
    Sleep(60)

    def lambda_4CE():
        OP_91(0xFE, 0xFFFFEF34, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4CE)
    Sleep(100)

    def lambda_4EE():
        OP_91(0xFE, 0xFFFFEF98, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4EE)
    Sleep(70)

    def lambda_50E():
        OP_91(0xFE, 0xFFFFEF98, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_50E)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #2
        0x101,
        "#1002F#6P果然亚妮拉丝也……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        (
            "#1069F#4P总之只能\x01",
            "先将她压制住了！\x02",
        )
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

    def lambda_5AE():
        OP_6D(-151500, 0, 500, 300)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5AE)

    def lambda_5C6():
        OP_6B(1760, 300)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5C6)
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
        (1, "loc_628"),
        (SWITCH_DEFAULT, "loc_62D"),
    )


    label("loc_628")

    OP_B4(0x0)
    Jump("loc_62D")

    label("loc_62D")

    Call(0, 10)
    Return()

    # Function_3_27F end

    def Function_4_632(): pass

    label("Function_4_632")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -154580, 1200, 1920, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_66F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_66F)
    OP_8F(0xFE, 0xFFFDA42C, 0x0, 0x780, 0x7D0, 0x0)
    Return()

    # Function_4_632 end

    def Function_5_690(): pass

    label("Function_5_690")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -154600, 1200, -1460, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_6CD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6CD)
    OP_8F(0xFE, 0xFFFDA418, 0x0, 0xFFFFFA4C, 0x7D0, 0x0)
    Return()

    # Function_5_690 end

    def Function_6_6EE(): pass

    label("Function_6_6EE")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -156040, 1200, 1040, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_72B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_72B)
    OP_8F(0xFE, 0xFFFD9E78, 0x0, 0x410, 0x7D0, 0x0)
    Return()

    # Function_6_6EE end

    def Function_7_74C(): pass

    label("Function_7_74C")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -156170, 1210, -750, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_789():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_789)
    OP_8F(0xFE, 0xFFFD9DF6, 0x0, 0xFFFFFD12, 0x7D0, 0x0)
    Return()

    # Function_7_74C end

    def Function_8_7AA(): pass

    label("Function_8_7AA")

    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x109, 16)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_7D5"),
        (5, "loc_7DD"),
        (3, "loc_7E5"),
        (4, "loc_7ED"),
        (6, "loc_7F5"),
        (7, "loc_7FD"),
        (SWITCH_DEFAULT, "loc_805"),
    )


    label("loc_7D5")

    SetChrChipByIndex(0xF8, 4)
    Jump("loc_805")

    label("loc_7DD")

    SetChrChipByIndex(0xF8, 6)
    Jump("loc_805")

    label("loc_7E5")

    SetChrChipByIndex(0xF8, 8)
    Jump("loc_805")

    label("loc_7ED")

    SetChrChipByIndex(0xF8, 10)
    Jump("loc_805")

    label("loc_7F5")

    SetChrChipByIndex(0xF8, 12)
    Jump("loc_805")

    label("loc_7FD")

    SetChrChipByIndex(0xF8, 14)
    Jump("loc_805")

    label("loc_805")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_826"),
        (5, "loc_82E"),
        (3, "loc_836"),
        (4, "loc_83E"),
        (6, "loc_846"),
        (7, "loc_84E"),
        (SWITCH_DEFAULT, "loc_856"),
    )


    label("loc_826")

    SetChrChipByIndex(0xF9, 4)
    Jump("loc_856")

    label("loc_82E")

    SetChrChipByIndex(0xF9, 6)
    Jump("loc_856")

    label("loc_836")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_856")

    label("loc_83E")

    SetChrChipByIndex(0xF9, 10)
    Jump("loc_856")

    label("loc_846")

    SetChrChipByIndex(0xF9, 12)
    Jump("loc_856")

    label("loc_84E")

    SetChrChipByIndex(0xF9, 14)
    Jump("loc_856")

    label("loc_856")

    SetChrFlags(0xF8, 0x1000)
    SetChrFlags(0xF9, 0x1000)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x109, 0x1000)

    def lambda_870():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_870)
    Sleep(50)

    def lambda_890():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_890)

    def lambda_8AB():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8AB)
    Sleep(50)

    def lambda_8CB():
        OP_91(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8CB)
    Return()

    # Function_8_7AA end

    def Function_9_8E1(): pass

    label("Function_9_8E1")

    SetChrChipByIndex(0x8, 17)

    def lambda_8EC():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_8EC)
    SetChrChipByIndex(0x9, 24)

    def lambda_90C():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_90C)
    Sleep(50)
    SetChrChipByIndex(0xA, 24)

    def lambda_931():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_931)
    SetChrChipByIndex(0xB, 26)

    def lambda_951():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_951)
    Sleep(50)
    SetChrChipByIndex(0xC, 26)

    def lambda_976():
        OP_91(0xFE, 0xDAC, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_976)
    Return()

    # Function_9_8E1 end

    def Function_10_98C(): pass

    label("Function_10_98C")

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
            "#1007F#6P亚、亚妮拉丝……\x02\x03",

            "#1019F好像变得\x01",
            "相当强的样子……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B61")

    ChrTalk(    #5
        0x103,
        (
            "#524F#4P嗯，为了不输给你，\x01",
            "一直在努力修练吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1025F#6P是嘛……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC2")

    ChrTalk(    #7
        0x106,
        (
            "#051F#4P嗯，为了不输给你，\x01",
            "一直在努力修练吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1025F#6P这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C27")

    ChrTalk(    #9
        0x103,
        (
            "#524F#4P嗯，为了不输给你，\x01",
            "一直在努力修练的样子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1025F#6P是嘛……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C8B")

    ChrTalk(    #11
        0x106,
        (
            "#051F#4P嗯，为了不输给你，\x01",
            "一直在努力修练的样子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1025F#6P这样啊……\x02",
    )

    CloseMessageWindow()

    label("loc_C8B")


    ChrTalk(    #13
        0x109,
        (
            "#1060F#4P好……\x01",
            "来把她唤醒吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CB5():
        OP_6D(-153380, 20, 1000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CB5)
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
        "#1312F#5P啊呜……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_99(0x8, 0x0, 0x3, 0x5DC)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E65")

    ChrTalk(    #15
        0x8,
        (
            "#1314F#5P嘿嘿……\x01",
            "艾丝蒂尔……前辈……\x02\x03",

            "还有凯文先生也……\x02\x03",

            "真的很谢谢\x01",
            "你们来救我……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7")

    label("loc_E65")


    ChrTalk(    #16
        0x8,
        (
            "#1314F#5P嘿嘿……艾丝蒂尔……\x02\x03",

            "还有凯文先生也……\x02\x03",

            "真的很谢谢\x01",
            "你们来救我……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB7")

    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    OP_0D()

    def lambda_ECD():
        OP_8F(0x109, 0xFFFDB26E, 0x14, 0x1CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ECD)

    ChrTalk(    #17
        0x101,
        (
            "#1025F#6P亚妮拉丝……\x01",
            "身体不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#1311F#5P嗯、嗯……\x01",
            "……没有问题哦……\x02\x03",

            "#812F话说回来……\x01",
            "卡露娜前辈他们……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA7")

    ChrTalk(    #19
        0x103,
        (
            "#021F#4P别担心，全员都救出来了。\x02\x03",

            "你是最后一个。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1033")

    label("loc_FA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEE")

    ChrTalk(    #20
        0x106,
        (
            "#051F#4P别担心，全员都救出来了。\x02\x03",

            "你是最后一个。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1033")

    label("loc_FEE")


    ChrTalk(    #21
        0x109,
        (
            "#1062F#4P别担心，全员都救出来了。\x02\x03",

            "#1061F亚妮拉丝是最后一个了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1033")


    ChrTalk(    #22
        0x8,
        (
            "#1314F#5P是、是吗……\x01",
            "太好了……\x02\x03",

            "#1316F对不起哦，艾丝蒂尔……\x02\x03",

            "难得约定要好一起战斗，\x01",
            "却变成这样……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1187")

    ChrTalk(    #23
        0x101,
        (
            "#1006F#6P不，别放在心上。\x02\x03",

            "都是多亏了亚妮拉丝你们，\x01",
            "我们才会知道这个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x103,
        (
            "#021F#4P你们已经充分地\x01",
            "完成了自己的工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x106,
        "#051F#4P之后就交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#1314F#5P艾丝蒂尔……\x01",
            "……前辈们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D4")

    label("loc_1187")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1260")

    ChrTalk(    #27
        0x101,
        (
            "#1006F#6P不，别放在心上。\x02\x03",

            "都是多亏了亚妮拉丝你们，\x01",
            "我们才会知道这个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#021F#4P你们已经充分地\x01",
            "完成了自己的工作哦。\x02\x03",

            "#020F之后就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#1314F#5P艾丝蒂尔……\x01",
            "……雪拉前辈……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D4")

    label("loc_1260")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1336")

    ChrTalk(    #30
        0x101,
        (
            "#1006F#6P不，别放在心上。\x02\x03",

            "都是多亏了亚妮拉丝你们，\x01",
            "我们才会知道这个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x106,
        (
            "#051F#4P你们已经充分地\x01",
            "完成了自己的工作哦。\x02\x03",

            "之后就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#1314F#5P艾丝蒂尔……\x01",
            "……阿加特前辈……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D4")

    label("loc_1336")


    ChrTalk(    #33
        0x101,
        (
            "#1006F#4P哪里，别放在心上。\x02\x03",

            "都是多亏了亚妮拉丝你们，\x01",
            "我们才会知道这个地方的。\x02\x03",

            "我认为你们已经充分地\x01",
            "完成了探索据点的工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "#1314F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    label("loc_13D4")

    OP_62(0x8, 0x12C, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #35
        0x8,
        (
            "#1317F#5P对、对了艾丝蒂尔！\x02\x03",

            "我……有件事\x01",
            "必须告诉你才行……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1004F#6P咦……什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#1317F#5P那个……那个……\x02\x03",

            "在、在逃跑的过程中，\x01",
            "我看见约修亚了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #38
        0x101,
        "#1020F#6P#5S！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1505")

    ChrTalk(    #39
        0x103,
        "#023F#4P咦咦！？\x02",
    )

    CloseMessageWindow()

    label("loc_1505")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152D")

    ChrTalk(    #40
        0x106,
        "#052F#4P你说什么！？\x02",
    )

    CloseMessageWindow()

    label("loc_152D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1551")

    ChrTalk(    #41
        0x105,
        "#043F#4P啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_1551")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1579")

    ChrTalk(    #42
        0x107,
        "#065F#4P哥、哥哥！？\x02",
    )

    CloseMessageWindow()

    label("loc_1579")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A3")

    ChrTalk(    #43
        0x108,
        "#073F#4P……那家伙……\x02",
    )

    CloseMessageWindow()

    label("loc_15A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C5")

    ChrTalk(    #44
        0x104,
        "#032F#4P唔……\x02",
    )

    CloseMessageWindow()

    label("loc_15C5")


    ChrTalk(    #45
        0x8,
        (
            "#813F#5P我在被士兵逼到无路可退时，\x01",
            "他就突然现身并破坏了包围……\x02\x03",

            "那身衣服和黑发我有印象，\x01",
            "应该不会错的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1026F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        "#1317F#5P艾丝蒂尔……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1016F#6P──啊。\x01",
            "嗯，抱歉……\x02\x03",

            "#1005F那、那么亚妮拉丝！\x01",
            "约修亚去了哪里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#813F#5P不知道……\x02\x03",

            "我当时也只顾着逃跑，\x01",
            "结果还是被抓住了……\x02\x03",

            "#812F但是……或许是\x01",
            "去了屋顶也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1020F#6P屋顶？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#812F#5P这座建筑物……屋顶好像有\x01",
            "飞艇的起降场……\x02\x03",

            "这里的士兵和研究员\x01",
            "好像都到那边去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1002F#6P是吗……明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        (
            "#1063F#4P亚妮拉丝。\x01",
            "你一个人可以逃出去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        "#816F#5P嗯……没问题。\x02",
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
            "#817F#5P这前面……\x01",
            "说不定还有什么埋伏……\x02\x03",

            "#812F大家……\x01",
            "要多加小心啊！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1897():

        label("loc_1897")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1897")

    QueueWorkItem2(0x101, 1, lambda_1897)

    def lambda_18A8():

        label("loc_18A8")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_18A8")

    QueueWorkItem2(0x109, 1, lambda_18A8)

    def lambda_18B9():

        label("loc_18B9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_18B9")

    QueueWorkItem2(0xF8, 1, lambda_18B9)

    def lambda_18CA():

        label("loc_18CA")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_18CA")

    QueueWorkItem2(0xF9, 1, lambda_18CA)

    def lambda_18DB():
        OP_6D(-144770, 0, -460, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18DB)
    OP_8E(0x8, 0xFFFDB20A, 0x14, 0xFFFFF5EC, 0x7D0, 0x0)

    def lambda_1907():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1907)
    OP_8E(0x8, 0xFFFDC074, 0x14, 0xFFFFF4F2, 0x9C4, 0x0)

    def lambda_1935():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1935)
    OP_8E(0x8, 0xFFFDCE98, 0xA, 0xFFFFFE02, 0x7D0, 0x0)

    def lambda_1963():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1963)
    OP_8E(0x8, 0xFFFDDB4A, 0xA, 0xFFFFFF60, 0x9C4, 0x0)

    def lambda_1991():
        OP_8E(0xFE, 0xFFFDE0C2, 0xA, 0xFFFFFF60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1991)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)

    def lambda_19D6():
        OP_6D(-150730, 20, 50, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19D6)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #56
        0x101,
        "#1026F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x109,
        (
            "#1065F#5P没想到，约修亚\x01",
            "竟然会来到这里……\x02\x03",

            "#1063F总之快前往屋顶吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1002F#5P……嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C0D)
    OP_28(0x98, 0x1, 0x100)
    OP_28(0x98, 0x1, 0x200)
    OP_28(0x98, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_10_98C end

    def Function_11_1A8D(): pass

    label("Function_11_1A8D")

    EventBegin(0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x0, 0x0, 0x3)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #59
        (
            "\x07\x02#1S『关于β』\x01",
            " \x01",
            "以利贝尔各地进行的实验结果为基础，\x01",
            "『β』的调整终于进入了最后的阶段。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_74(0x0, 0x0, 0x1)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #60
        (
            "\x07\x02#1S这是完全模仿\x01",
            "原来机能的仿真器，\x01",
            "导力场的同步率也超过９０％。\x01",
            "就结果来说，尺寸虽然扩大了，\x01",
            "但要完成『福音计划』……（※以下删除）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0B")
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #61
        "\x07\x00得到了\x1F\xFC\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FC, 1)
    Sleep(500)

    label("loc_1C0B")

    OP_A2(0x1C0E)
    OP_28(0x98, 0x1, 0x800)
    OP_74(0x0, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x1)
    Return()

    # Function_11_1A8D end

    def Function_12_1C2A(): pass

    label("Function_12_1C2A")

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
        (0, "loc_1CA7"),
        (1, "loc_1CAD"),
        (SWITCH_DEFAULT, "loc_1CB3"),
    )


    label("loc_1CA7")

    OP_A2(0x1200)
    Jump("loc_1CB3")

    label("loc_1CAD")

    OP_A2(0x1201)
    Jump("loc_1CB3")

    label("loc_1CB3")

    Return()

    # Function_12_1C2A end

    def Function_13_1CB4(): pass

    label("Function_13_1CB4")

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

    # Function_13_1CB4 end

    SaveToFile()

Try(main)
